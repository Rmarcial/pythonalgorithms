"""
Fibonacci's rabbit puzzle:
  at month 0 there are two young rabbits (one male, one female)
  rabbits turn adult and mate at one month
  rabbits have one month gestation period
  assume rabbits never die and female produce one male and one female
    every month from their second on

  how many rabbits are there in one year?
"""


# Iterative - Computes the number of rabbits at a given month
def rabbits_iter(month):
    young = 2
    adult = 0

    for n in range(int(month)):
        adult += young
        young = adult - young

    return young + adult


# Recursive - Computes the number of rabbits at a given month
def rabbits_recur(month):
    if month == 0 or month == 1:
        return 2
    else:
        return rabbits_recur(month - 2) + rabbits_recur((month - 1))


# Recursive with dictionary - prevent several computations of the same value
def rabbits_recur_dict(month):
    computed_dict = {0: 2, 1: 2}

    def compute(mth, dic):
        if mth in dic:
            return dic[mth]
        else:
            dic[mth] = compute(mth - 2, dic) + compute(mth - 1, dic)
            return dic[mth]

    return compute(month, computed_dict)


# Tests
nr = 32
print(rabbits_iter(nr))
print(rabbits_recur(nr))
print(rabbits_recur_dict(nr))
