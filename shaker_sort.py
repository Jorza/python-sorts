def comparison(val1, val2, reverse):
    return val1 > val2 if reverse else val1 < val2


def swap_items(in_list, idx1, idx2):
    temp = in_list[idx1]
    in_list[idx1] = in_list[idx2]
    in_list[idx2] = temp


def shaker_sort(in_list, key=None, reverse=False):

    # If a key is given, construct the key for each element of the list
    if key is not None:
        key_list = [key(entry) for entry in in_list]
    else:
        # If no key is defined, set key_list to input list. Modifications to key_list will now sort the original list.
        key_list = in_list

    left_mark = 0
    right_mark = len(in_list) - 1
    while left_mark < right_mark:
        # Bubble largest left to right
        last_unsorted_index = None
        for i in range(left_mark, right_mark):
            if comparison(in_list[i+1], in_list[i], reverse):
                if key is not None:
                    swap_items(in_list, i, i+1)
                swap_items(key_list, i, i+1)
                last_unsorted_index = i

        if last_unsorted_index is None:
            break
        else:
            right_mark = last_unsorted_index

        # Bubble smallest right to left
        last_unsorted_index = None
        for i in range(right_mark, left_mark, -1):
            if comparison(in_list[i], in_list[i-1], reverse):
                if key is not None:
                    swap_items(in_list, i, i+1)
                swap_items(key_list, i, i+1)
                last_unsorted_index = i

        if last_unsorted_index is None:
            break
        else:
            left_mark = last_unsorted_index
