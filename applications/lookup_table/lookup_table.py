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


resCache = {}
powCache= {}
factCache= {}
divCache= {}
modCache= {}

def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    # this is not my code. i just pasted it to study and try to understand this problem. which i still do not.
    
    if (x,y) not in powCache:
        powCache[(x,y)] = math.pow(x, y)
    v= powCache[(x,y)]
    print(v)

    if (x,y) not in factCache:
        factCache[(x,y)]= math.factorial(powCache[x,y])
    v = factCache[(x,y)]
    print(v)

    if (x,y) not in divCache:
        divCache[(x,y)]= factCache[(x,y)]//= (x,y)
    v //= (x + y)
    print(v)

    v %= 982451653
    print(v)

    cache[(x,y)]= v
    return v

print('building table')
for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    cache[(x,y)]= slowfun(x,y)
print('done building table')

# Do not modify below this line!
for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x}, {y}: {slowfun(x, y)}')


# print(slowfun_too_slow(3, 2))
