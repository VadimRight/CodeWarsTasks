import functools

cache = {}


def func_cache(func):
    @functools.wraps(func)
    def wrapper(x):
        if x not in cache:
            result = func(x)
            cache[x] = result
        else:
            result = cache[x]
        return result
    return wrapper


@func_cache
def function_x(x):
    return x*5


print(function_x(2))