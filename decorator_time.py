import time

def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        total = time.time() - start_time
        print(
            f'Function {func.__name__} took {total:.4f} seconds to run'
        )
        return result
    return wrapper

@timeit
def test_function(x):
    return sum([i * x for i in range(100000)])

print(test_function(2))

class TimeItClass:
    def __init__(self, func):
        self.func = func
    
    def __call__(self, *args, **kwargs):
        start_time = time.time()
        result = self.func(*args, **kwargs)
        total = time.time() - start_time
        print(
            f'Function {self.func.__name__} took {total:.4f} seconds to run'
        )
        return result

@TimeItClass
def test_function_2(x):
    return sum([i * x for i in range(100000)])

print(test_function_2(2))
