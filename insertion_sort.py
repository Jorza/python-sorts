# Insertion sort functions
def comparison(val1, val2, reverse):
    return val1 < val2 if reverse else val1 > val2


def swap_values(in_list, idx1, idx2):
    temp = in_list[idx1]
    in_list[idx1] = in_list[idx2]
    in_list[idx2] = temp


def insertion_sort(in_list, key=None, reverse=False):
    """
    Mimics behaviour of .sort() for lists, but also returns the sorted list.
    :param in_list: The list to be sorted.
    :param key: Optional argument. A function that will be run on each element of in_list.
    The result will be used to order in_list.
    :param reverse: Optional argument. If omitted, sorts in ascending order. Set to 'True' for descending order.
    :return: The sorted list.
    """

    # If a key is given, construct the key for each element of the list
    if key is not None:
        key_list = [key(entry) for entry in in_list]
    else:
        # If no key is defined, set key_list to input list. Modifications to key_list will now sort the original list.
        key_list = in_list

    for i in range(len(in_list)):
        j = i
        while comparison(key_list[j-1], key_list[j], reverse) and j > 0:
            if key is not None:
                # If key_list is defined, must update in_list separately.
                # If key_list = in_list, it is only necessary to swap elements in key_list.
                swap_values(in_list, j - 1, j)
            swap_values(key_list, j-1, j)
            j -= 1
    return in_list
