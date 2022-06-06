import time
import functools

@functools.lru_cache(maxsize=100)
def fib(n):
    if n <= 2:
        result = n
    else:
        result = fib(n - 1) + fib(n - 2)
    return result


def time_of_execution(n: int):
    start=time.time()
    fib(n)
    stop=time.time()
    return stop-start


for i in range(1,35):
    print(f"time for fib({i}) = {time_of_execution(i)}")
