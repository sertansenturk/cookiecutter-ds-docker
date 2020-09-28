import abc
import logging
from pathlib import Path

from ..mlflow_common import log

logger = logging.Logger(__name__)  # pylint: disable-msg=C0103
logger.setLevel(logging.INFO)


class Data(abc.ABC):
    """abstract class to extract-transform-load data
    """
    EXPERIMENT_NAME = None
    RUN_NAME = None

    def __init__(self):
        """instantiates an Audio object
        """
        self.tmp_dir = None

    def _tmp_dir_path(self) -> Path:
        """returns the path of the temporary directory, where the audio files
        are downloaded

        Returns
        -------
        Path
            path of the temporary directory
        """
        return Path(self.tmp_dir.name)

    @abc.abstractmethod
    def from_mlflow(self):
        pass

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
        pass

    def _cleanup(self):
        """deletes the temporary directory, where the audio files are
        downloaded
        """
        self.tmp_dir.cleanup()
