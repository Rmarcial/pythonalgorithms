"""
 Implementation of the bisection search algorithm to find if an element is in a list
"""


def bisection_search1(el, lst):
    """
    bisection search strategy: O(n log n) n is length of the list
    list slicing costs O(n) because it makes list copies
    :param el: element to search for in the list
    :param lst: list of elements
    :return: True if list contains element
    """
    if lst == []:
        return False

    elif len(lst) == 1:
        return lst[0] == el

    else:
        lst.sort()

        while True:
            middle = len(lst) // 2

            if lst[middle] == el:
                return True
            elif lst[middle] > el:
                return bisection_search1(el, lst[:middle])
            else:
                return bisection_search1(el, lst[middle:])


def bisection_search(el, lst):
    """
    bisection search strategy: O(log n) n is length of the list
    uses list limits in the search, instead of slicing, to avoid copies
    :param el: element to look for in the list
    :param lst: list
    :return: True if list contains element
    """

    # searches for element in a sorted list
    def bi_search(el, lst, low, high):
        if low == high:
            return el == lst[low]
        else:
            middle = (low + high) // 2
            if el == lst[middle]:
                return True
            elif el < lst[middle]:
                return bi_search(el, lst, low, middle - 1)
            else:
                return bi_search(el, lst, middle + 1, high)

    if not lst:  # empty list
        return False
    else:
        lst.sort()
        low = 0
        high = len(lst) - 1
        return bi_search(el, lst, low, high)


# Tests
elements = [10, 20]
print(bisection_search(21, elements))


