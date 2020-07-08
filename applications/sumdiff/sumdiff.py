"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

# q = set(range(1, 10))
# q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

# Your code here


def equalCombos(orderedNumSet):
  pass
  # iterate and store set into a dict?

  # returns a list of equal combos
  # by checking through a dict to get equal combos stored?


# left side (addition)
# list from L-R
a = f(1) + f(3)

# right side(subtraction)
# list from R-L
b = f(12) - f(7)

# compare the sides
if a == b:
    pass

if __name__ == '__main__':
    print(equalCombos(q)

    print("")
