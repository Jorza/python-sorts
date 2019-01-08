class MinHeap:
    def __init__(self, values, key):
        self.values = values
        self.heap = []
        self.key = key
        self.build_heap()

    def swap_values(self, in_list, idx1, idx2):
        temp = in_list[idx1]
        in_list[idx1] = in_list[idx2]
        in_list[idx2] = temp

    def parent(self, index):
        return (index - 1) // 2 if index > 0 else 0

    def left_child(self, index):
        left_child_index = 2 * index + 1
        return left_child_index if left_child_index < len(self.heap) - 1 else index

    def right_child(self, index):
        right_child_index = 2 * index + 2
        return right_child_index if right_child_index < len(self.heap) - 1 else index

    def small_child(self, index):
        left_child = self.left_child(index)
        right_child = self.right_child(index)
        return left_child if self.key(self.heap[left_child]) < self.key(self.heap[right_child]) else right_child

    # Append and up-heap a single element.
    def insert(self, value):
        self.heap.append(value)
        up_heap_idx = len(self.heap) - 1
        parent_idx = self.parent(up_heap_idx)
        while self.key(self.heap[up_heap_idx]) < self.key(self.heap[parent_idx]):
            self.swap_values(self.heap, up_heap_idx, parent_idx)
            up_heap_idx = parent_idx
            parent_idx = self.parent(up_heap_idx)

    # Insert all values into a min-heap.
    def build_heap(self):
        for value in self.values:
            self.insert(value)

    # Extract the minimum item, down-heap the last item.
    def extract(self):
        self.swap_values(self.heap, 0, len(self.heap) - 1)
        down_heap_idx = 0
        small_child_idx = self.small_child(down_heap_idx)
        while self.key(self.heap[down_heap_idx]) > self.key(self.heap[small_child_idx]):
            self.swap_values(self.heap, down_heap_idx, small_child_idx)
            down_heap_idx = small_child_idx
            small_child_idx = self.small_child(down_heap_idx)
        return self.heap.pop()

    # Extract all items in ascending order.
    def empty_heap(self, reverse=False):
        value_list = []
        while len(self.heap) > 0:
            value_list.append(self.extract())
        if reverse:
            reverse_list = []
            for item in value_list:
                reverse_list.append(item)
            value_list = reverse_list
        return value_list


def heap_sort(in_list, key=None, reverse=False):
    # If a key is not given, construct the key to return its argument.
    if key is None:
        key = lambda x: x

    # Use a min-heap to sort the list. Modify the list in-place.
    heap = MinHeap(in_list, key)
    in_list.clear()
    in_list += heap.empty_heap(reverse)


# test cases
from random import shuffle
start_list = ['A','B','C','D','E','F','a','b','c','d','e','f','!','{','',' ','1','2','3','4','5']
start_list.sort()

test_list = start_list[:]

shuffle(test_list)
print(test_list)
heap_sort(test_list)
print(test_list)

print(start_list)

print("success" if test_list == start_list else "fail")