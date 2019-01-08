# Selection sort functions
def comparison(val1, val2, reverse):
    return val1 > val2 if reverse else val1 < val2


def find_target_idx(in_list, start, stop, reverse):
    target_idx = start
    for idx in range(start + 1, stop):
        if comparison(in_list[idx], in_list[target_idx], reverse):
            target_idx = idx
    return target_idx


def swap_values(in_list, idx1, idx2):
    temp = in_list[idx1]
    in_list[idx1] = in_list[idx2]
    in_list[idx2] = temp


def selection_sort(in_list, key=None, reverse=False):
    """
    Mimics behaviour of .sort() for lists, but also returns the sorted list.
    :param in_list: The list to be sorted.
    :param key: Optional argument. A function that will be run on each element of in_list.
    The result will be used to order in_list.
    :param reverse: Optional argument. If omitted, sorts in ascending order. Set to 'True' for descending order.
    :return: The sorted list.
    """
    stop = len(in_list)

    # If a key is given, construct the key for each element of the list
    if key is not None:
        key_list = [key(entry) for entry in in_list]
    else:
        # If no key is defined, set key_list to input list. Modifications to key_list will now sort the original list.
        key_list = in_list

    for index in range(stop):
        # Find position of the target item in key_list: index of minimum value; if reverse is 'True', index of maximum.
        target_idx = find_target_idx(key_list, index, stop, reverse)

        # Swap numbers at “index” and “target_idx”
        # If a key is given, swap for the full list, and also in the key list
        # If key_list = in_list, it is only necessary to swap elements in key_list.
        if key is not None:
            swap_values(in_list, index, target_idx)
        swap_values(key_list, index, target_idx)

    return in_list
