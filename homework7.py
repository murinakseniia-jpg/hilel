def shout(func):
    def wrapper(value):
        result = func(value)
        return result.upper()
    return wrapper

@shout
def add_suffix(value):
    return value + "suffix"

def positive_only(func):
    def wrapper(*args):
        for arg in args:
            if not isinstance(arg, (int, float)) or arg <= 0:
                raise ValueError
        return func(*args)
    return wrapper

@positive_only
def add_two(x):
    return x + 2