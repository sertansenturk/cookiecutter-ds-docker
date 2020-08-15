import os
from unittest import mock

from {{ cookiecutter.package_name }}.config import config


class TestRead:
    @mock.patch.object(config.configparser.ConfigParser, 'read')
    def test_read(self, mock_read):
        # WHEN
        config.read()

        # THEN
        mock_read.assert_called_once_with(config._get_config_filepath())


def test_get_config_filepath():
    # WHEN
    path = config._get_config_filepath()

    # THEN
    assert os.path.exists(path)
