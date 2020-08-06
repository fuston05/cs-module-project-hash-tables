# Your code here
import math
import random


def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    print(v)

    v = math.factorial(v)
    print(v)

    v //= (x + y)
    print(v)

    v %= 982451653
    print(v)

    return v


cache = {}

def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    # this is not my code. i just pasted it to study and try to understand this problem. which i still do not.
    v = 0
    if v not in cache:

        cache[v] = math.pow(x, y)
        print(v)

        cache[v] = math.factorial(v)
        print(v)

        cache[v] //= (x + y)
        print(v)

        cache[v] %= 982451653
        print(v)

    return cache[v]


# Do not modify below this line!
for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x}, {y}: {slowfun(x, y)}')


# print(slowfun_too_slow(3, 2))
