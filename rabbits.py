"""
Fibonacci's rabbit puzzle:
  at month 0 there are two young rabbits (one male, one female)
  rabbits turn adult and mate at one month
  rabbits have one month gestation period
  assume rabbits never die and female produce one male and one female
    every month from their second on

  how many rabbits are there in one year?
"""


# Iterative - Computes the number of rabbits at some month
def rabbits_iter(month):
    young = 2
    adult = 0

    for n in range(int(month)):
        adult += young
        young = adult - young

    return young + adult


# Recursive - Computes the number of rabbits at some month
def rabbits_recur(month):
    if month == 0 or month == 1:
        return 2
    else:
        return rabbits_recur(month-2) + rabbits_recur((month-1))


# Tests
print(rabbits_iter(41))
print(rabbits_recur(41))



