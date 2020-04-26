"""
Implementation of the recursive algorithm to solve Hanoi Towers
"""


def print_move(fr, to):
    print("move from", fr, "to", to)


"""
In order to move stack N from A to B, using C as spare:
1 - move stack N-1 from A to C, using B as spare;
2 - move one disk (the biggest) from A to B, using C as spare (not needed);
3 - move stack N-1 from C to B, using A as spare.
"""
def hanoi(n, fr, to, spare):
    if n == 1:
        print_move(fr, to)
    else:
        hanoi(n-1, fr, spare, to)    # 1
        hanoi(1, fr, to, spare)      # 2
        hanoi(n-1, spare, to, fr)    # 3


# Tests
hanoi(200, 'A', 'B', 'C')