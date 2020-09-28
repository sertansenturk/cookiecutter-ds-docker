from unittest import mock

import pytest

from {{ cookiecutter.package_name }}.data.data import Data


@pytest.fixture
def mock_tmp_dir(scope="session") -> mock.MagicMock:
    tmp_dir = mock.MagicMock()
    tmp_dir.name = "/tmp/dir_path"

    return tmp_dir


class TestData:
    @mock.patch.multiple(Data, __abstractmethods__=set())
    def test_cleanup(self):
        # GIVEN
        data = Data()

        # WHEN; THEN
        with mock.patch.object(data, "tmp_dir"):
            with mock.patch.object(data.tmp_dir,
                                   "cleanup"
                                   ) as mock_cleanup:
                data._cleanup()
        mock_cleanup.assert_called_once_with()

    @mock.patch.multiple(Data, __abstractmethods__=set())
    def test_log(self, mock_tmp_dir):
        # GIVEN
        data = Data()

        # WHEN; THEN
        with mock.patch("{{ cookiecutter.package_name }}.data.data.log"
                        ) as mock_log:
            with mock.patch.object(data,
                                   "tmp_dir",
                                   mock_tmp_dir):
                with mock.patch.object(data,
                                       "_cleanup"
                                       ) as mock_cleanup:
                    data.log()

                    mock_log.assert_called_once_with(
                        experiment_name=data.EXPERIMENT_NAME,
                        run_name=data.RUN_NAME,
                        artifact_dir=data._tmp_dir_path(),
                        tags=data._mlflow_tags())

                    mock_cleanup.assert_called_once_with()
