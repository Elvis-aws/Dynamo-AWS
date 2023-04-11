import os
from pathlib import Path
from utils.rapper_function import func_loger

path = Path(__file__)
ROOT_DIR = path.parent.absolute()


def get_configini_file_path():
    config_path = os.path.join(ROOT_DIR, "config.ini")
    return config_path


def get_file_path(relative_path):
    config_path = os.path.join(ROOT_DIR, relative_path)
    return config_path
