import configparser
from configurations.filePath import get_configini_file_path
from utils.rapper_function import func_loger

config = configparser.RawConfigParser()
config_path = get_configini_file_path()
config.read(config_path)


class ReadConfig:

    @staticmethod
    @func_loger
    def get_employee_url():
        url = config.get('common info', 'employee_url')
        return url

    @staticmethod
    @func_loger
    def get_all_employee_url():
        url = config.get('common info', 'all_employee_url')
        return url

