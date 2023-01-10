import os
from pathlib import Path
path = Path(__file__)
ROOT_DIR = path.parent.absolute()


def get_configini_file_path():
    config_path = os.path.join(ROOT_DIR, "config.ini")
    return config_path
