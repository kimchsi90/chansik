import heapq


def heap_sort(iterable):
    h = []
    sorted_h = []

    for i in iterable:
        heapq.heappush(h, i)
    for i in range(len(h)):
        sorted_h.append(heapq.heappop(h))

    return sorted_h

result = heap_sort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)
