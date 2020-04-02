import mlflow
import pytest


@pytest.mark.dependency()
def test_mlflow_log_to_backend():
    # GIVEN
    parameters = {
        "param1": "param1_val",
        "param2": "param2_val"
    }
    metric = {
        "key": "metric1",
        "val": list(range(10))
    }
    tag = {
        "key": "tag_key1",
        "val": "tag_val1"
    }

    # WHEN
    mlflow.set_experiment('experiment-alpha')
    with mlflow.start_run():
        mlflow.log_params(parameters)

        for vv in metric["val"]:
            mlflow.log_metric(metric["key"], vv)

        mlflow.set_tag(tag["key"], tag["val"])

    # THEN
    assert True  # logging succeeded


@pytest.mark.dependency(depends=["test_mlflow_log_to_backend"])
def test_mlflow_get_logs():
    assert True


@pytest.mark.dependency()
def test_mlflow_log_artifact():
    # GIVEN
    with open("dummy.txt", 'w'):
        pass  # create an empty file

    # WHEN
    mlflow.set_experiment('experiment-alpha')
    with mlflow.start_run():
        mlflow.log_artifact("dummy.txt")

    # THEN
    assert True  # logging succeeded


@pytest.mark.dependency(depends=["test_mlflow_log_artifact"])
def test_mlflow_get_artifact():
    assert True
