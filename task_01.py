from typing import Callable, Dict


def caching_fibonacci() -> Callable[[int], int]:
    cache: Dict[int, int] = {}

    def fibonacci(n: int) -> int:
        if n in cache:
            return cache[n]

        if n <= 1:
            return n

        result = fibonacci(n - 2) + fibonacci(n - 1)
        cache[n] = result

        return result

    return fibonacci


# testing


fib = caching_fibonacci()

assert fib(-1) == -1
assert fib(1) == 1
assert fib(2) == 1
assert fib(3) == 2
assert fib(10) == 55
assert fib(15) == 610
