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
