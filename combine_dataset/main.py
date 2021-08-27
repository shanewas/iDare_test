import numpy as np
import pandas as pd
import time
from functools import wraps


def logger(func):
    import logging
    logging.basicConfig(filename='log/{}.log'.format(
        func.__name__), level=logging.INFO)

    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return func(*args, **kwargs)

    return wrapper


def timer(func):
    import time

    @wraps(func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(func.__name__, t2))
        return result

    return wrapper


@logger
@timer
def dataset_combiner(df1, df2):
    df3 = pd.merge(df1, df2)
    return df3


df1 = pd.DataFrame({'employee': ['Bob', 'Jake', 'Lisa', 'Sue'],
                    'group': ['Accounting', 'Engineering', 'Engineering', 'HR']})

df2 = pd.DataFrame({'employee': ['Lisa', 'Bob', 'Jake', 'Sue'],
                    'hire_date': [2004, 2008, 2012, 2014]})
print(dataset_combiner(df1, df2))
