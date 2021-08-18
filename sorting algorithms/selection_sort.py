def selection_sort (lst):
    """
    Arranges the elements of list lst in ascending order.
    Physically rearranges the elements of lst.
    """
    n = len(lst)
    for i in range(n - 1):
        small = i
        # for i element in list check all j elements upward to be less than i
        for j in range(i + 1, n):
            if lst[j] < lst[small]:
                small = j
        if small != i:
            # exchange lst[i] with lst[small]
            lst[i], lst[small] = lst[small], lst[i]