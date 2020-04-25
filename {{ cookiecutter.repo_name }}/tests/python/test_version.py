import {{ cookiecutter.package_name }}

def test_version():
    assert {{ cookiecutter.package_name }}.__version__, "version not found"
