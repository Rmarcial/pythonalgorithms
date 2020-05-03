"""
 Implementation of the bisection search algorithm to find if an element is in a list
"""
import random
import time

def bisection_search1(el, lst):
    """
    bisection search strategy: O(n log n). n is length of the list
    list slicing costs O(n) because it makes list copies
    :param el: element to search for in the list
    :param lst: list of elements
    :return: True if list contains element
    """
    if lst == []:
        return False

    elif len(lst) == 1:
        return el == lst[0]

    else:
        lst.sort()
        middle = len(lst) // 2
        if el == lst[middle]:
            return True
        elif el < lst[middle]:
            return bisection_search1(el, lst[:middle])
        else:
            return bisection_search1(el, lst[middle + 1:])


def bisection_search(element, element_list):
    """
    bisection search strategy: O(log n) n is length of the list
    uses list limits in the search, instead of slicing, to avoid copies
    :param element: element to look for in the list
    :param element_list:
    :return: True if list contains element
    """

    # searches for element in a sorted list
    def bi_search(el, lst, low, high):

        if low == high:  # size 1 list
            return el == lst[low]
        else:
            middle = (low + high) // 2
            if el == lst[middle]:
                return True
            elif el < lst[middle]:
                high = middle
                return bi_search(el, lst, low, high)
            else:
                low = middle + 1
                return bi_search(el, lst, low, high)

    if not element_list:  # empty list
        return False
    else:
        element_list.sort()
        low_index = 0
        high_index = len(element_list) - 1
        return bi_search(element, element_list, low_index, high_index)


# Tests
el_list1 = []

start = time.clock()
for n in range(100000000):
    el_list1.append(random.randint(0, 500))
stop = time.clock()

print("start:", start)
print("stop:", stop)
print(" time to make list:", stop - start, "seg")
print()

start = time.clock()
print(bisection_search1(1, el_list1))
stop = time.clock()
print("bs1 time:", stop - start, "seg")

print()

start = time.clock()
print(bisection_search(1, el_list1))
stop = time.clock()
print("bs time:", stop - start, "seg")
