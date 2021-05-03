import abc
import logging
from pathlib import Path
from typing import Optional, List

import mlflow

from ..config import config
from ..mlflow_common import get_run_by_name, log

logger = logging.Logger(__name__)  # pylint: disable-msg=C0103
logger.setLevel(logging.INFO)

cfg = config.read()


class Data(abc.ABC):
    """abstract class to extract-transform-load data
    """
    EXPERIMENT_NAME = cfg.get("mlflow", "data_processing_experiment_name")
    RUN_NAME = None
    FILE_EXTENSION = '.ext'  # dummy extension

    def __init__(self):
        """instantiates a Data object
        """
        self.tmp_dir: Optional[Path] = None

    def _tmp_dir_path(self) -> Path:
        """returns the path of the temporary directory, where the artifact
        files are stored

        Returns
        -------
        Path
            path of the temporary directory
        """
        return Path(self.tmp_dir.name)

    def _cleanup(self):
        """deletes the temporary directory, where the artifact files are
        stored
        """
        self.tmp_dir.cleanup()

    @classmethod
    def from_mlflow(cls) -> List[str]:
        """return artifact file paths from the relevant mlflow run
        Returns
        -------
        List[Path]
            path of the artifacts logged in mlflow
        Raises
        ------
        ValueError
            if the run does not exist
        """
        mlflow_run = get_run_by_name(cls.EXPERIMENT_NAME, cls.RUN_NAME)
        if mlflow_run is None:
            raise ValueError("Artifacts are not logged in mlflow")

        client = mlflow.tracking.MlflowClient()
        artifacts = client.list_artifacts(mlflow_run.run_id)
        artifact_names = [ff.path for ff in artifacts
                          if ff.path.endswith(cls.FILE_EXTENSION)]

        artifact_paths = [client.download_artifacts(mlflow_run.run_id, an)
                          for an in artifact_names]

        logger.info("Returning the paths of %d artifacts.",
                    len(artifact_paths))

        return artifact_paths

    def log(self):
        """Logs the artifacts to an mlflow run with appropriate tags

        Raises
        ------
        ValueError
            If a run with the same experiment and run name is already logged
            in mlflow
        """
        log(experiment_name=self.EXPERIMENT_NAME,
            run_name=self.RUN_NAME,
            artifact_dir=self._tmp_dir_path(),
            tags=self._mlflow_tags())
        logger.info("Logged artifacts & tags to mlflow under experiment %s, "
                    "run %s", self.EXPERIMENT_NAME, self.RUN_NAME)

        self._cleanup()

    @abc.abstractmethod
    def _mlflow_tags(self):
        """returns tags to log onto a mlflow run

        Returns
        -------
        Dict
            tags to log
        """
