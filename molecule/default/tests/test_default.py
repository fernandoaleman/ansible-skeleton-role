# molecule/default/tests/test_default.py
from utils import load_role_vars

vars = load_role_vars()

test_file = vars["test_file"]


def test_host_is_reachable(host):
    etc = host.file(test_file)
    assert etc.exists
    assert etc.is_directory
