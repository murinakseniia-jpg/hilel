def log_args(func):
    def wrapper(*args):
        print(args)
        return func(*args)

    return wrapper

@log_args
def add(a, b):
    return a + b


def repeat(times):
    def decorator(func):
        def wrapper(*args):
            for _ in range(times):
                func(*args)
        return wrapper
    return decorator

@repeat(3)
def say_hello():
    print("Hello!")


words = ["apple", "cat", "banana", "dog", "house"]

for word in words:
    if (length := len(word)) > 4:
        print(word, length)


def countdown(n):
    while n > 0:
        yield n
        n -= 1
    yield "Start!"