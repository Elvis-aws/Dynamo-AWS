import random

from utils.rapper_function import func_loger


@func_loger
def get_gender():
    random_index = random.randint(0, 1)
    if random_index == 1:
        return 'Female'
    else:
        return 'Male'
