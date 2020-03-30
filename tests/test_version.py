import template_repo

def test_version():
    assert template_repo.__version__, "version not found"
