import configparser
import os


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


def _get_config_filepath() -> str:
    """returns the path of the mr{{ cookiecutter.package_name }}e configuration file

    Returns
    -------
    str
        path of the {{ cookiecutter.package_name }} configuration file
    """
    return os.path.join(os.path.dirname(__file__), 'config.ini')
