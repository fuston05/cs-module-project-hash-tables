"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

# q = set(range(1, 10))
# q = set(range(1, 200))
q = (1, 3, 4, 7, 12)

def f(x):
    return x * 4 + 6


# loop over original 

    
    # find all possible combinations of 4
    # on each combo of 4:
        # every possible combo of 2 using the f(x)
        # store the 2 numbers and the value after the addition or subtraction

    # repeat for subtraction side

    # loop addition against subtraction dict's
    # if a+b == c-d:
    # build the following string output:
        # f(1) + f(1) = f(12) - f(7)    10 + 10 = 54 - 34

addition= {}


subtraction= {}



answer= ''

print(answer)