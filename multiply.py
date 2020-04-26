"""
2 implementations of the mathematical product of two positive integers, using:
    - interation
    - recursion
"""


# Interative Product
def prod_iter(a, b):
    result = 0
    while b > 0:
        result += a
        b -= 1
    return result


# Recursive Product
def prod_recur(a, b):
    if b == 0:
        return 0
    elif b == 1:
        return a
    else:
        return a + prod_recur(a, b-1)


# Tests
print(prod_iter(6, 7))
print(prod_recur(6, 7))



