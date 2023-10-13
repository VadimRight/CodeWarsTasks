def invert(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, list):
            result = list(map(abs, result))
        return result

    return wrapper

@invert
def foo(length):
    if length == 0:
        return [0]
    is_minus = length < 0
    return [i for i in range(abs(length)) if i % 2 == 0]


print(foo(10))
print(foo(-10))
# foo(-8)
