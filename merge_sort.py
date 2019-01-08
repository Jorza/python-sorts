# merge_sort functions
def comparison(val1, val2, reverse):
    return val1 > val2 if reverse else val1 < val2


def merge_lists(a_list, b_list, key=None, reverse=False):

    # If a key is not given, construct the key to return its argument
    if key is None:
        key = lambda x: x

    a_idx, b_idx = 0, 0
    merged_list = []

    # Take lowest values from starts of lists
    while a_idx < len(a_list) and b_idx < len(b_list):
        if comparison(key(a_list[a_idx]), key(b_list[b_idx]), reverse):
            merged_list.append(a_list[a_idx])
            a_idx += 1
        else:
            merged_list.append(b_list[b_idx])
            b_idx += 1

    # If one list is empty, append all remaining values in other list.
    if a_idx < len(a_list):
        merged_list += a_list[a_idx:]
    elif b_idx < len(b_list):
        merged_list += b_list[b_idx:]

    return merged_list


def merge_sort(in_list, start=0, end=None, key=None, reverse=False):
    if end is None:
        end = len(in_list)

    if end - start <= 1:
        return [in_list[start]]
    else:
        mid_idx = (start + end) // 2

        left_list = merge_sort(in_list, start, mid_idx, key=key, reverse=reverse)
        right_list = merge_sort(in_list, mid_idx, end, key=key, reverse=reverse)

        return merge_lists(left_list, right_list, key=key, reverse=reverse)


from random import shuffle
start_list = ['A','B','C','D','E','F','a','b','c','d','e','f','!','{','',' ','1','2','3','4','5']
test_list = start_list[:]

start_list.sort(reverse=True)

shuffle(test_list)
print(test_list)
sorted_list = merge_sort(test_list, reverse=True)
print(sorted_list)

print(start_list)

print("success" if sorted_list == start_list else "fail")
