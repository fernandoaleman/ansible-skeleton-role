# molecule/default/tests/test_default.py
from utils import load_role_vars

vars = load_role_vars()

etc_dir = vars["etc_dir"]


def test_host_is_reachable(host):
    """Ensure etc directory exists"""
    etc = host.file(etc_dir)
    assert etc.exists
    assert etc.is_directory
