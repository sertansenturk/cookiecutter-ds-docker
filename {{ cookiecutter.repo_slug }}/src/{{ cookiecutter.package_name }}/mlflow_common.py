import logging

from typing import Dict, Optional

import mlflow
import pandas as pd

logger = logging.Logger(__name__)  # pylint: disable-msg=C0103
logger.setLevel(logging.INFO)


def get_run_by_name(experiment_name: str, run_name: str) -> pd.Series:
    """Returns the mlflow run metadata from the experiment and run name

    Parameters
    ----------
    experiment_name : str
        mlflow experiment name
    run_name : str
        mlflow run name (stored as a mlflow.runName tag)

    Returns
    -------
    pd.Series
        None, if the run does not exist (annotations haven't been logged)
        run information storing the annotations

    Raises
    ------
    ValueError
        If there is more a single run with the same name
    """
    # Check if the artifact is logged in mlflow
    experiment = mlflow.get_experiment_by_name(experiment_name)
    if experiment is not None:
        annotation_runs = mlflow.search_runs(
            experiment_ids=experiment.experiment_id,
            filter_string=f"tags.mlflow.runName = '{run_name}'")

        if annotation_runs.empty:
            logger.warning("No runs with the name %s in experiment %s",
                           run_name, experiment_name)
            return None

        if len(annotation_runs) > 1:
            raise ValueError(
                "There are more than one runs for %s: %s . Please "
                "inspect the run in the mlflow UI and manually make "
                "necessary corrections."
                % (run_name, ', '.join(annotation_runs.run_id)))

        return annotation_runs.iloc[0]

    logger.warning("Experiment %s does not exist.", experiment_name)
    return None


def log(experiment_name: str,
        run_name: str,
        artifact_dir: Optional[str] = None,
        tags: Optional[Dict] = None):

    mlflow_run = get_run_by_name(experiment_name, run_name)
    if mlflow_run is not None:
        raise ValueError(
            "There is already a run for %s:%s. Overwriting is not "
            "permitted. Please delete the run manually if you want "
            "to log the annotations again."
            % (run_name, mlflow_run.run_id))

    mlflow.set_experiment(experiment_name)
    with mlflow.start_run(run_name=run_name):
        mlflow.set_tags(tags)
        mlflow.log_artifacts(artifact_dir)
