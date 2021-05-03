import importlib
import logging


def get_jupyter_logger(name: str,
                       level: int = logging.INFO
                       ) -> logging.Logger:
    """creates a logger object for jupyter notebooks using basic config

    Parameters
    ----------
    name : str
        name of the logger
    level : int, optional
        logger level, by default logging.INFO

    Returns
    -------
    logging.Logger
        logger object set for Jupyter notebooks
    """
    # fix the strange logging startup configuration in iPython
    # see: https://stackoverflow.com/a/21475297
    importlib.reload(logging)
    logging.basicConfig(level=level)

    # create logger
    logger = logging.getLogger(name)
    logger.setLevel(level)

    return logger
