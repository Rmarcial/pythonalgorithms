"""
 3 Different implementations of the Heron of Alexandria's method to compute
 square root

 2 Methods to compute cube roots:
    - method of Approximation
    - Bissection search
"""

# Iterative with fixed number of iterations
def sqrt_a(x):
    
    guess = 1
    n_iterations = range(100)
       
    for i in n_iterations:

        if guess * guess != x:
            guess = (guess + x/guess) / 2
        else:
            return guess
            
    return guess


# Iterative with variable number of iterations until some tolerable error is
# achieved
def sqrt_b(x):

    ERROR_LIMIT = 0.0001    # precision of the calculation
    guess = 1

    while not good_enough(guess, x, ERROR_LIMIT):
        guess = improve_guess(guess, x)

    return guess


# Recursive until a tolerable error is achieved
def sqrt_recur(x):
    ERROR_LIMIT = 0.0001
    guess = 1

    def sqrt_r(x, g):
        return g if good_enough(g, x, ERROR_LIMIT) else sqrt_r( x, improve_guess(g, x))

    return sqrt_r(x, guess)


# Method of Approximation to cube root within a certain error
def cubrt_ap(x):
    INCREMENT = 0.0001
    ERROR_LIMIT = 0.01
    guess = 0.0

    while module(cube(guess) - x) > ERROR_LIMIT and guess < x:
        guess += INCREMENT
        print(guess)

    return guess


# Bissection Search to compute cube root within a certain error
def cubrt_bs(x):
    ERROR_LIMIT = 0.001
    high_boundary = x
    low_boundary = 0.0
    guess = average(high_boundary, low_boundary)

    while module(cube(guess) - x) > ERROR_LIMIT:

        if(cube(guess) > x):
            high_boundary = guess
            guess = average(high_boundary, low_boundary)
            print("greater")

        elif(cube(guess < x)):
            low_boundary = guess
            guess = average(high_boundary, low_boundary)
            print("less")

        else:
            return guess



# Auxiliary methods
def module(x):
    return -x if x < 0 else x


def square(x):
    return x*x


def cube(x):
    return x*x*x


def average(x, y):
    return (x + y) / 2.0


def good_enough(guess, x, error_limit):
    return True if module( square(guess) - x) < error_limit else False


def improve_guess(guess, x):
    return average(guess, x/guess)



# Tests
print (cubrt_bs(27))

