import importlib.util
from pathlib import Path
import unittest
from uuid import uuid4

path = Path(__file__).resolve().parents[1] / 'skills/workflow-handoff/scripts/validate_handoff.py'
spec = importlib.util.spec_from_file_location('validator', path)
v = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)

def base():
    return dict(schema_version=1,packet_id=str(uuid4()),workflow_id='search-review',title='Search review',objective='Resume a design review',created_at='2026-10-26T17:00:00+01:00',supersedes=None,author='Alex',recipient='Morgan',current_owner='Alex',harness='Codex',state='offered',ready_for_resume=True,scope='design',brief=dict(url='https://example.org/brief',version='v1',accessible_verified=True),repositories=[],artifacts=[],demo=dict(mode='none',reference=None,steps=[]),changes=[],decisions=[],open_questions=[],checks=[],next_steps=['Review the lifecycle'],blockers=[],slack=dict(channel_id='C123ABC',thread_ts=None,message_url=None))

class Checks(unittest.TestCase):
    def test_design_only(self): self.assertEqual(v.validate(base(),True),[])
    def test_local_unshared(self):
        p=base();p['brief']['url']='http://localhost:3001';self.assertTrue(v.validate(p))
    def test_dirty_repo(self):
        p=base();p['scope']='prototype';p['repositories']=[dict(url='https://example.org/repo',branch='feature',commit='a'*40,dirty=True,published_verified=True)];self.assertTrue(v.validate(p))
    def test_unpublished(self):
        p=base();p['repositories']=[dict(url='https://example.org/repo',branch='feature',commit='a'*40,dirty=False,published_verified=False)];self.assertTrue(v.validate(p))
    def test_browser_state(self):
        p=base();p['demo']['mode']='browser-only';self.assertTrue(v.validate(p))
    def test_fixture(self):
        p=base();p['demo']=dict(mode='fixture',reference='https://example.org/fixture/v1',steps=['Load the example']);self.assertTrue(v.validate(p));p['artifacts']=[dict(name='fixture',url=p['demo']['reference'],accessible_verified=True)];self.assertEqual(v.validate(p),[])
    def test_blocked_draft(self):
        p=base();p.update(state='blocked',ready_for_resume=False,blockers=['Code not shared']);p['brief']['url']=None;self.assertEqual(v.validate(p),[]);self.assertTrue(v.validate(p,True))
    def test_self_reference(self):
        p=base();p['supersedes']=p['packet_id'];self.assertTrue(v.validate(p))
    def test_bad_shapes(self):
        for key in ('brief','demo','repositories','artifacts','slack','changes'):
            p=base();p[key]=None;self.assertTrue(v.validate(p),key)
    def test_timezone(self):
        p=base();p['created_at']='2026-10-26T17:00:00';self.assertTrue(v.validate(p))
    def test_credentials(self):
        p=base();p['brief']['url']='https://user:secret@example.org/x';self.assertTrue(v.validate(p))
    def test_code_requires_repo(self):
        p=base();p['scope']='prototype';self.assertTrue(v.validate(p))

class MalformedPacketTests(unittest.TestCase):
    def test_rejects_malformed_or_local_urls(self):
        for url in ("https://localhost./x", "https://127.0.0.2/x", "https://[::1]/x",
                    "https://0.0.0.0/x", "https://127.1/x", "https://2130706433/x",
                    "https://bad host/x", "https://example.org:bad/x", "https://example.org:0/x",
                    "https://example.org:99999/x", "https://@example.org/x", "https://example..org/x"):
            with self.subTest(url=url):
                p = base(); p['brief']['url'] = url
                self.assertTrue(v.validate(p))

    def test_shared_internal_hosts_remain_allowed(self):
        for url in ("https://docs.example.org:8443/x", "https://10.0.0.5/x", "https://docs.corp/x"):
            self.assertTrue(v.shared_url(url))

    def test_draft_metadata_is_still_typed(self):
        for field, value in (("accessible_verified", "false"), ("version", {"revision": 1})):
            p = base(); p['ready_for_resume'] = False; p['state'] = 'draft'
            p['brief'][field] = value
            self.assertTrue(v.validate(p))

    def test_boolean_is_not_schema_version(self):
        p = base(); p['schema_version'] = True
        self.assertTrue(v.validate(p))

    def test_artifact_name_is_nonempty_text(self):
        for name in (' ', {'name': 'fixture'}):
            p = base(); p['artifacts'] = [dict(name=name, url='https://example.org/x', accessible_verified=True)]
            self.assertTrue(v.validate(p))

    def test_uuid_case_cannot_hide_self_reference(self):
        p = base(); p['supersedes'] = p['packet_id'].upper()
        self.assertTrue(v.validate(p))

    def test_unshared_brief_needs_blocker_even_with_repo(self):
        p = base(); p.update(state='draft', ready_for_resume=False)
        p['brief'] = dict(url=None, version=None, accessible_verified=False)
        p['repositories'] = [dict(url='https://example.org/repo', branch='main', commit='a'*40, dirty=False, published_verified=True)]
        self.assertTrue(v.validate(p))

if __name__=='__main__': unittest.main()
