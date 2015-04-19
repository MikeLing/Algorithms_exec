left = lambda i: i * 2
right = lambda i: i * 2 + 1
parent = lambda i: i / 2
pos = lambda i: i - 1


class Heap(list):

    def __init__(self, A):
        self.heap_size = len(A)
        self.extend(A)

    def to_list(self):
        return list(self)

    def length(self):
        return len(self)

    def swap(self, i, j):
        self[pos(i)], self[pos(j)] = self[pos(j)], self[pos(i)]

    def pos(self, i):
        return self[pos(i)]


def max_heapify(heap, i):
    l, r = left(i), right(i)

    if l <= heap.heap_size and heap.pos(l) > heap.pos(i):
        largest = l
    else:
        largest = i

    if r <= heap.heap_size and heap.pos(r) > heap.pos(largest):
        largest = r

    if largest != i:
        heap.swap(i, largest)
        max_heapify(heap, largest)


def build_max_heap(A):
    heap = Heap(A)

    for i in range(int(heap.length() / 2), 0, -1):
        max_heapify(heap, i)

    return heap


def heap_sort(A):
    heap = build_max_heap(A)

    for i in range(heap.length(), 1, -1):
        heap.swap(i, 1)
        heap.heap_size -= 1
        max_heapify(heap, 1)

    return heap

