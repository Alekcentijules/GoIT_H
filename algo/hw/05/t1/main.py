from typing import Callable

def caching_fibonacci():
    cache = {}
    def fibonacci(n):
        nonlocal cache
        if n <= 0: 
            return 0
        elif n == 1:
            return 1
        elif n in cache:
            return cache[n]
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]
    return fibonacci

fibon = caching_fibonacci()
print(fibon(10))
# print(fibon(22))
# print(fibon(22))