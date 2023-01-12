from utils import api_logger

logger = api_logger.loggen()


def func_loger(func):
    def wrap(*args, **kwargs):
        status_codes = [200, 201, 202, 204, 400, 409, 500]
        logger.info(f'{func.__name__}  execution started')
        result = func(*args, **kwargs)
        if kwargs.__len__() != 0:
            logger.info(f'payload: {kwargs}')
        try:
            _status_codes = [x for x in status_codes if x == result.status_code]
            logger.info(f'{result.text}, status_code: {_status_codes}')
        except:
            pass
        logger.info(f'{func.__name__}  execution successful')
        return result

    return wrap
