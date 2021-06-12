from functools import wraps


def dec_type_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        li = [i for i in (*args, *kwargs.values())]
        n = [f'{func.__name__}({i}:{type(i)})' for i in li]
        print(*n, *func(*args, **kwargs), sep=";\n", end=".\n")

    return wrapper


@dec_type_logger
def calc(*args, **kwargs):
    li = [i for i in (*args, *kwargs.values()) if isinstance(i, int) or isinstance(i, float)]
    return [i ** 3 for i in li]


calc(2, 4, {'ints': 4}, {2, 4}, (5, 'sh'), [7, 3], 'str', name='Nick')
