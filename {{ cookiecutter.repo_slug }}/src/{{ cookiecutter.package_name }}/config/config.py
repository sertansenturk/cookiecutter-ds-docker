import configparser
from pathlib import Path


def read() -> configparser.ConfigParser:
    """reads {{ cookiecutter.package_name }} configuration file and returns the parser

    Returns
    -------
    configparser.ConfigParser
        configparser with {{ cookiecutter.package_name }} configuration
    """
    cfg = configparser.ConfigParser()
    config_file = _get_config_filepath()
    cfg.read(config_file)

    return cfg


def _get_config_filepath() -> Path:
    """returns the path of the mr{{ cookiecutter.package_name }}e configuration file

    Returns
    -------
    pathlib.Path
        path of the {{ cookiecutter.package_name }} configuration file
    """
    return Path(Path(__file__).parent, 'config.ini')
