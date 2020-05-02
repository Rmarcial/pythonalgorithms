"""
 Implementation of the binary search algorithm to find if an element is in a list
"""


def binary_search(el, lst):
    """
    binary search strategy: O(log n) n is length of the list
    :param el: element to search for in the list
    :param lst: list of elements
    :return: True if list contains element
    """
    if not lst:
        return False

    else:
        lst.sort()

        while True:
            middle = len(lst) // 2

            if lst[middle] == el:
                return True
            elif lst[middle] > el:
                return binary_search(el, lst[:middle])
            else:
                return binary_search(el, lst[middle+1:])


# Tests
elements = [3, 1, 2, -23, 5, 342324324, 0]
print(binary_search(-24, elements))


