"""
ALGORITHM

If list is empty return None
Check element in the middle of the list
    if element is target element return element position
    if element is larger than the element we are looking for
        perform a binary search on the first half
    if element is smaller than the element we are looking for
        perform a binary search on the the second half of the list

"""

def binary_search(lst, seek):
    """
        DESCRIPTION: returns the index of element seek in the list lst
        if seek is present in lst.
        Return None if seek is not an element of the list lst
        lst is the list in which to search
        seek is the element to find
        NB: lst must be a sorted list
    """

    #initialize two pointers, the first element in the list and the last element in the list
    #The pointers are keeping track of the first and last element in the list
    first = 0
    last = len(lst) - 1
    while first <= last: #if list is empty, first is 0 and last is 0 - 1; the while condition is not met hence it returns None
        mid = first + (last - first+1) // 2 #nb: integer division; first + (last - first+1) ensures that first ≤ mid ≤ last.
        if seek == mid: return mid
        elif seek > mid: last = mid -1
        else: first = mid + 1
    return None