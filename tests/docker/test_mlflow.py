import mlflow


def test_mlflow_log_to_backend():
    mlflow.set_experiment('experiment-alpha')
    with mlflow.start_run():
        mlflow.log_param("param1", "param1_val")
        mlflow.log_param("param2", "param2_val")

        for i in range(10):
            mlflow.log_metric("metric1", i)

        mlflow.set_tag("tag_key", "tag_val")

    assert True
