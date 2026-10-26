#!/usr/bin/env python3
"""Offline packet checks. No network, credential access, writes or command execution."""
import argparse
from datetime import datetime
import json
from pathlib import Path
import re
from urllib.parse import urlparse
from uuid import UUID


def shared_url(value):
    if not isinstance(value, str):
        return False
    try:
        u = urlparse(value)
        host = (u.hostname or '').lower()
        return (u.scheme == 'https' and bool(host) and not u.username and not u.password
                and host not in ('localhost', '127.0.0.1', '::1') and not host.endswith('.localhost'))
    except ValueError:
        return False


def validate(p, require_ready=False):
    errors = []
    def check(ok, msg):
        if not ok:
            errors.append(msg)
    if not isinstance(p, dict):
        return ['Packet must be a JSON object']
    check(p.get('schema_version') == 1, 'Unsupported schema_version')
    for k in ('title', 'objective', 'author', 'recipient', 'current_owner', 'harness'):
        check(isinstance(p.get(k), str) and bool(p[k].strip()), f'{k} is required')
    check(isinstance(p.get('workflow_id'), str) and bool(re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', p['workflow_id'])), 'workflow_id must be a slug')
    for k in ('packet_id', 'supersedes'):
        if k == 'supersedes' and p.get(k) is None:
            continue
        try:
            UUID(p.get(k, ''))
        except (ValueError, TypeError, AttributeError):
            errors.append(f'{k} must be a UUID')
    check(p.get('packet_id') != p.get('supersedes'), 'Packet cannot supersede itself')
    try:
        d = datetime.fromisoformat(p.get('created_at', '').replace('Z', '+00:00'))
        check(d.tzinfo is not None, 'created_at needs timezone')
    except (ValueError, TypeError, AttributeError):
        errors.append('created_at must be ISO 8601')
    check(p.get('state') in ('draft', 'offered', 'accepted', 'blocked', 'completed'), 'Invalid state')
    check(p.get('scope') in ('review', 'design', 'prototype', 'backend', 'frontend', 'mixed'), 'Invalid scope')
    check(type(p.get('ready_for_resume')) is bool, 'ready_for_resume must be boolean')
    for k in ('changes', 'decisions', 'open_questions', 'checks', 'next_steps', 'blockers'):
        check(isinstance(p.get(k), list) and all(isinstance(x, str) and x.strip() for x in p[k]), f'{k} must be a list of nonempty strings')
    check(bool(p.get('next_steps')), 'At least one next step is required')
    ready = require_ready or p.get('ready_for_resume') is True
    if require_ready:
        check(p.get('ready_for_resume') is True, '--ready requires ready_for_resume=true')
    brief = p.get('brief')
    if not isinstance(brief, dict):
        errors.append('brief must be an object')
        brief = {}
    if brief.get('url') is not None:
        check(shared_url(brief['url']), 'brief.url must be a shared HTTPS URL without credentials')
    repos = p.get('repositories')
    if not isinstance(repos, list):
        errors.append('repositories must be a list')
        repos = []
    for i, r in enumerate(repos):
        if not isinstance(r, dict):
            errors.append(f'repositories[{i}] must be an object')
            continue
        check(shared_url(r.get('url')), f'repositories[{i}].url must be an HTTPS repository URL')
        check(isinstance(r.get('branch'), str) and bool(r['branch'].strip()), f'repositories[{i}].branch required')
        check(isinstance(r.get('commit'), str) and bool(re.fullmatch(r'[0-9a-f]{40}|[0-9a-f]{64}', r['commit'])), f'repositories[{i}].commit must be full SHA')
        check(type(r.get('dirty')) is bool and type(r.get('published_verified')) is bool, f'repositories[{i}] needs dirty and published_verified booleans')
        if ready:
            check(r.get('dirty') is False and r.get('published_verified') is True, f'repositories[{i}] is not clean and verified published')
    artifacts = p.get('artifacts')
    if not isinstance(artifacts, list):
        errors.append('artifacts must be a list')
        artifacts = []
    for i, a in enumerate(artifacts):
        if not isinstance(a, dict):
            errors.append(f'artifacts[{i}] must be an object')
            continue
        check(bool(a.get('name')) and shared_url(a.get('url')), f'artifacts[{i}] needs name and shared HTTPS URL')
        check(type(a.get('accessible_verified')) is bool, f'artifacts[{i}].accessible_verified must be boolean')
        if ready:
            check(a.get('accessible_verified') is True, f'artifacts[{i}] access is unverified')
    demo = p.get('demo')
    if not isinstance(demo, dict):
        errors.append('demo must be an object')
        demo = {}
    check(demo.get('mode') in ('none', 'fixture', 'instructions', 'browser-only'), 'Invalid demo mode')
    check(isinstance(demo.get('steps'), list) and all(isinstance(x, str) and x.strip() for x in demo.get('steps', [])), 'demo.steps must be strings')
    if demo.get('mode') in ('fixture', 'instructions'):
        check(shared_url(demo.get('reference')) and bool(demo.get('steps')), 'Demo fixture/instructions need shared reference and steps')
        if ready:
            check(any(isinstance(a, dict) and a.get('url') == demo.get('reference') and a.get('accessible_verified') is True for a in artifacts), 'Demo reference needs a verified artifact entry')
    slack = p.get('slack')
    if not isinstance(slack, dict):
        errors.append('slack must be an object')
    else:
        for key, pattern in [('channel_id', r'[CG][A-Z0-9]+'), ('thread_ts', r'\d+\.\d+')]:
            check(slack.get(key) is None or (isinstance(slack[key], str) and bool(re.fullmatch(pattern, slack[key]))), f'Invalid slack.{key}')
        check(slack.get('message_url') is None or shared_url(slack['message_url']), 'Invalid Slack message URL')
    if ready:
        check(shared_url(brief.get('url')) and bool(brief.get('version')) and brief.get('accessible_verified') is True, 'Ready requires a verified shared brief and version')
        check(not p.get('blockers'), 'Ready packet has blockers')
        check(p.get('state') != 'blocked', 'Blocked state cannot be ready')
        check(demo.get('mode') != 'browser-only', 'Browser-only state is not reproducible')
        if p.get('scope') in ('prototype', 'backend', 'frontend', 'mixed'):
            check(bool(repos), 'Implementation handoff requires repositories')
    elif not repos and not brief.get('url'):
        check(bool(p.get('blockers')), 'Unavailable shared work needs an explicit blocker')
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('packet', type=Path)
    parser.add_argument('--ready', action='store_true')
    args = parser.parse_args()
    try:
        packet = json.loads(args.packet.read_text(encoding='utf-8'))
        errors = validate(packet, args.ready)
    except (OSError, ValueError) as e:
        print(json.dumps({'valid': False, 'errors': [str(e)]}))
        return 1
    print(json.dumps({'valid': not errors, 'errors': errors, 'note': 'Offline structural checks only; verify remote state and authorization separately.'}, indent=2))
    return bool(errors)


if __name__ == '__main__':
    raise SystemExit(main())
