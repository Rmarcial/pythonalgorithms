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
        return rabbits_recur(month-2) + rabbits_recur((month-1))


# Recursive with dictionary - prevent several computations of the same value
def rabbits_recur_dict(month):
    computations_dict = {}

    def compute(mth, dic):
        if mth == 0 or mth == 1:
            return 2
        else:
            if mth-2 in dic and mth-1 in dic:
                return dic[mth - 2] + dic[mth - 1]
            else:
                dic[mth - 2] = compute(mth - 2, dic)
                dic[mth - 1] = compute(mth - 1, dic)
                return dic[mth - 2] + dic[mth - 1]

    return compute(month, computations_dict)


# Tests
nr = 37
print(rabbits_iter(nr))
print(rabbits_recur(nr))
print(rabbits_recur_dict(nr))


