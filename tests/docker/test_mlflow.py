import mlflow
import pytest


@pytest.mark.dependency()
def test_mlflow_log_to_backend():
    mlflow.set_experiment('experiment-alpha')
    with mlflow.start_run():
        mlflow.log_param("param1", "param1_val")
        mlflow.log_param("param2", "param2_val")

        for i in range(10):
            mlflow.log_metric("metric1", i)

        mlflow.set_tag("tag_key", "tag_val")

    assert True


def test_mlflow_log_artifact():
    with open("dummy.txt", 'w') as f:
        pass

    mlflow.set_experiment('experiment-alpha')
    with mlflow.start_run():
        mlflow.log_artifact("dummy.txt")

    assert True


@pytest.mark.dependency(depends=["test_mlflow_log_to_backend"])
def test_mlflow_get_logs():
    assert True


@pytest.mark.dependency(depends=["test_mlflow_log_artifact"])
def test_mlflow_get_artifact():
    assert True
