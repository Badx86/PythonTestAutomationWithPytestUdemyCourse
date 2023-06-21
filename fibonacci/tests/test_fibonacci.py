from typing import Callable
import pytest
from fibonacci.cached import fibonacci_cached
from fibonacci.naive import fibonacci_naive


@pytest.mark.parametrize("fib_func", [fibonacci_naive, fibonacci_cached])
@pytest.mark.parametrize("n,expected", [(0, 0), (1, 1), (2, 1), (20, 6765)])
def test_fibonacci(fib_func: Callable[[int], int], n: int, expected: int) -> None:
    res = fib_func(n)
    assert res == expected
