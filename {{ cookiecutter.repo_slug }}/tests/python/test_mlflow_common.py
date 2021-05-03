from unittest import mock

import pytest

import pandas as pd
import {{ cookiecutter.package_name }}
from pandas.testing import assert_series_equal


@pytest.fixture
def mock_experiment(scope="session") -> mock.MagicMock:
    experiment = mock.MagicMock()
    experiment.experiment_id = "mock_id"
    return experiment


class TestMlflow:
    @mock.patch("{{ cookiecutter.package_name }}.mlflow_common.logger.warning")
    def test_get_run_by_name_no_experiment(self, mock_warning):
        # GIVEN
        experiment_name = "exp_name"
        run_name = "run_name"

        # WHEN
        with mock.patch('mlflow.get_experiment_by_name',
                        autospec=True,
                        return_value=None):
            result = {{ cookiecutter.package_name }}.mlflow_common.get_run_by_name(
                experiment_name, run_name)

        # THEN
        mock_warning.assert_called_once()
        assert result is None

    @mock.patch("{{ cookiecutter.package_name }}.mlflow_common.logger.warning")
    def test_get_run_by_name_no_run(self, mock_warning, mock_experiment):
        # GIVEN
        mock_runs = pd.DataFrame(columns=["run_id"])  # empty
        experiment_name = "exp_name"
        run_name = "run_name"

        # WHEN
        with mock.patch('mlflow.get_experiment_by_name',
                        autospec=True,
                        return_value=mock_experiment):
            with mock.patch('mlflow.search_runs',
                            autospec=True,
                            return_value=mock_runs):
                result = {{ cookiecutter.package_name }}.mlflow_common.get_run_by_name(
                    experiment_name, run_name)

        # THEN
        mock_warning.assert_called_once()
        assert result is None

    @mock.patch("{{ cookiecutter.package_name }}.mlflow_common.logger.warning")
    def test_get_run_by_name_multi_runs(self, mock_warning, mock_experiment):
        # GIVEN
        mock_runs = pd.DataFrame([{"run_id": "rid1"}, {"run_id": "rid2"}])
        experiment_name = "exp_name"
        run_name = "run_name"

        # WHEN; THEN
        with mock.patch('mlflow.get_experiment_by_name',
                        autospec=True,
                        return_value=mock_experiment):
            with mock.patch('mlflow.search_runs',
                            autospec=True,
                            return_value=mock_runs):
                with pytest.raises(ValueError):
                    {{ cookiecutter.package_name }}.mlflow_common.get_run_by_name(
                        experiment_name, run_name)

    def test_get_run_by_name_single_run(self, mock_experiment):
        # GIVEN
        mock_run_dict = {"run_id": "rid1"}
        mock_runs = pd.DataFrame([mock_run_dict])
        experiment_name = "exp_name"
        run_name = "run_name"

        # WHEN
        with mock.patch('mlflow.get_experiment_by_name',
                        autospec=True,
                        return_value=mock_experiment):
            with mock.patch('mlflow.search_runs',
                            autospec=True,
                            return_value=mock_runs):
                result = {{ cookiecutter.package_name }}.mlflow_common.get_run_by_name(
                    experiment_name, run_name)

        # THEN
        expected = pd.Series(mock_run_dict)
        assert_series_equal(result, expected, check_names=False)

    @mock.patch("mlflow.start_run")
    @mock.patch("mlflow.set_experiment")
    def test_log_existing_run(self,
                              mock_mlflow_set_experiment,
                              mock_mlflow_start_run):
        # GIVEN
        experiment_name = "exp_name"
        run_name = "run_name"
        artifact_dir = "tmp_dir"
        tags = {"key1": "val1"}
        mock_run = pd.DataFrame([{"run_id": "rid"}])

        # WHEN; THEN
        with mock.patch("{{ cookiecutter.package_name }}.mlflow_common.get_run_by_name",
                        return_value=mock_run):
            with pytest.raises(ValueError):
                {{ cookiecutter.package_name }}.mlflow_common.log(
                    experiment_name=experiment_name,
                    run_name=run_name,
                    artifact_dir=artifact_dir,
                    tags=tags
                )

            mock_mlflow_set_experiment.assert_not_called()
            mock_mlflow_start_run.assert_not_called()

    @mock.patch("mlflow.log_artifacts")
    @mock.patch("mlflow.set_tags")
    @mock.patch("mlflow.start_run")
    @mock.patch("mlflow.set_experiment")
    def test_log_no_run(self,
                        mock_mlflow_set_experiment,
                        mock_mlflow_start_run,
                        mock_mlflow_set_tags,
                        mock_mlflow_log_artifacts,
                        mock_experiment):
        # GIVEN
        experiment_name = "exp_name"
        run_name = "run_name"
        artifact_dir = "tmp_dir"
        tags = {"key1": "val1"}
        mock_run = pd.DataFrame(columns=["run_id"])  # empty

        # WHEN; THEN
        with mock.patch('mlflow.get_experiment_by_name',
                        autospec=True,
                        return_value=mock_experiment):
            with mock.patch('mlflow.search_runs',
                            autospec=True,
                            return_value=mock_run):
                {{ cookiecutter.package_name }}.mlflow_common.log(
                    experiment_name=experiment_name,
                    run_name=run_name,
                    artifact_dir=artifact_dir,
                    tags=tags
                )

                mock_mlflow_set_experiment.assert_called_once()
                mock_mlflow_start_run.assert_called_once()

                mock_mlflow_set_tags.assert_called_once()
                mock_mlflow_log_artifacts.assert_called_once_with(
                    artifact_dir)

    @mock.patch("mlflow.log_artifacts")
    @mock.patch("mlflow.set_tags")
    @mock.patch("mlflow.start_run")
    @mock.patch("mlflow.set_experiment")
    def test_log_no_experiment(self,
                               mock_mlflow_set_experiment,
                               mock_mlflow_start_run,
                               mock_mlflow_set_tags,
                               mock_mlflow_log_artifacts):
        # GIVEN
        experiment_name = "exp_name"
        run_name = "run_name"
        artifact_dir = "tmp_dir"
        tags = {"key1": "val1"}

        # WHEN; THEN
        with mock.patch('mlflow.get_experiment_by_name',
                        autospec=True,
                        return_value=None):
            {{ cookiecutter.package_name }}.mlflow_common.log(
                experiment_name=experiment_name,
                run_name=run_name,
                artifact_dir=artifact_dir,
                tags=tags
            )

            mock_mlflow_set_experiment.assert_called_once()
            mock_mlflow_start_run.assert_called_once()

            mock_mlflow_set_tags.assert_called_once()
            mock_mlflow_log_artifacts.assert_called_once_with(
                artifact_dir)
