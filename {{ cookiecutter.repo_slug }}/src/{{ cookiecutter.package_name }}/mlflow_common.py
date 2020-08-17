import logging

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
