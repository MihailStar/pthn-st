# 1
from itertools import count
from typing import Generator

g = (-x for x in count(1))

for _ in range(20):
    number = next(g)
    print(number)

assert number == -20


def gen() -> Generator[int, None, None]:
    for x in count(1):
        yield -x


g_2 = gen()

for _ in range(20):
    number_2 = next(g_2)
    print(number_2)

assert number_2 == -20

for _ in range(20):
    number = next(g)
    print(number)

assert number == -40


# 2
from itertools import chain, count

fib_0, fib_2 = 0, 1
a, b = fib_0, fib_2


def fibonacci() -> Generator[int, None, None]:
    for _ in count(1):
        global a
        global b

        c = a + b

        a = b
        b = c

        yield c


gen_fib = chain((fib_0, fib_2), fibonacci())

for _ in range(20):
    print(next(gen_fib))

assert next(gen_fib) == 6765
