import configparser
from configurations.filePath import get_configini_file_path
config = configparser.RawConfigParser()
config_path = get_configini_file_path()
config.read(config_path)


class ReadConfig:

    @staticmethod
    def get_employee_url():
        url = config.get('common info', 'employee_url')
        return url

    @staticmethod
    def get_all_employee_url():
        url = config.get('common info', 'all_employee_url')
        return url

