# quick_sort functions
def comparison(val1, val2, reverse):
    return val1 > val2 if reverse else val1 < val2


def swap_values(in_list, idx1, idx2):
    temp = in_list[idx1]
    in_list[idx1] = in_list[idx2]
    in_list[idx2] = temp


def partition(in_list, start, end, pivot_idx=None, key=None, reverse=False):

    # If a key is not given, construct the key to return its argument
    if key is None:
        key = lambda x: x

    # Swap pivot to start index

    # If pivot not given, or is out of range
    if pivot_idx is None or pivot_idx < start or pivot_idx >= end:
        pivot_idx = start

    # pivot_idx is specified as a valid index in the range, use that element as the pivot.
    if pivot_idx != start:
        swap_values(in_list, start, pivot_idx)
    pivot = key(in_list[start])

    # Record right-most value smaller/bigger than the pivot, iterate through list.
    small_item_idx = start
    for new_item_idx in range(start, end):
        if comparison(key(in_list[new_item_idx]), pivot, reverse):
            # Swap new small/big value to position to the right of last small/big value
            small_item_idx += 1
            swap_values(in_list, small_item_idx, new_item_idx)

    # Swap pivot to its sorted position
    swap_values(in_list, start, small_item_idx)

    return small_item_idx


def quick_sort(in_list, start=0, end=None, key=None, reverse=False):

    if end is None:
        end = len(in_list)

    if end - start > 1:
        pivot_idx = partition(in_list, start, end, key=key, reverse=reverse)
        quick_sort(in_list, start, pivot_idx, key=key, reverse=reverse)
        quick_sort(in_list, pivot_idx + 1, end, key=key, reverse=reverse)


# test cases
from random import shuffle
start_list = ['A','B','C','D','E','F','a','b','c','d','e','f','!','{','',' ','1','2','3','4','5']
start_list.sort()

test_list = start_list[:]

shuffle(test_list)
print(test_list)
quick_sort(test_list)
print(test_list)

print(start_list)

print("success" if test_list == start_list else "fail")
