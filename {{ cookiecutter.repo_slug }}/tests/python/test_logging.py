import {{ cookiecutter.package_name }}


def test_get_jupyter_logger():
    # GIVEN
    name = "logger_name"

    # WHEN
    result = {{ cookiecutter.package_name }}.logging.get_jupyter_logger(name)

    # THEN
    assert result.name == name


def test_get_jupyter_logger_level():
    # GIVEN
    name = "logger_name"
    level = 30  # logging.WARNING

    # WHEN
    result = {{ cookiecutter.package_name }}.logging.get_jupyter_logger(name, level)

    # THEN
    assert result.level == level
