from unittest import mock

import pytest

import mlflow
import pandas as pd

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
    @mock.patch("{{ cookiecutter.package_name }}.data.data.get_run_by_name",
                return_value=None)
    def test_from_mlflow_no_run(self, mock_run):
        # GIVEN
        data = Data()

        # WHEN; THEN
        with pytest.raises(ValueError):
            data.from_mlflow()
        mock_run.assert_called_once()

    @mock.patch.multiple(Data, __abstractmethods__=set())
    def test_from_mlflow(self):
        # GIVEN
        data = Data()
        mock_run = pd.Series({"run_id": "rid1"})
        artifact_names = ["data1.ext",
                          "data2.ext"]

        # WHEN; THEN
        mock_list = []
        mock_calls = []
        for an in artifact_names:
            tmp_call = mock.MagicMock()
            tmp_call.path = an
            mock_list.append(tmp_call)
            mock_calls.append(mock.call(mock_run.run_id, an))

        with mock.patch("{{ cookiecutter.package_name }}.data.data.get_run_by_name",
                        return_value=mock_run):
            with mock.patch('mlflow.tracking.MlflowClient.__init__',
                            autospec=True,
                            return_value=None):
                with mock.patch.object(mlflow.tracking.MlflowClient,
                                       "list_artifacts",
                                       autospec=True,
                                       return_value=mock_list):
                    with mock.patch.object(mlflow.tracking.MlflowClient,
                                           "download_artifacts"
                                           ) as mock_download_artifacts:
                        _ = data.from_mlflow()
                        mock_download_artifacts.assert_has_calls(mock_calls)

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
