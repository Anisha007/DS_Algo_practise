"""
1. kth largest element in an array
2. kth smallest element in an array
"""
import heapq

data = [4, 5, 3, 2, 1, 6, 4, 3, 8, 9]
k = 3
min_heap = data[:k]
heapq.heapify(min_heap)
# print(min_heap)
for i in range(k, len(data)):
    if data[i] < min_heap[0]:
        continue
    heapq.heappushpop(min_heap, data[i])
# print(min_heap[0])

data_comp = [ele * -1 for ele in data]
max_heap_in_terms_of_min_heap = data_comp[:k]
heapq.heapify(max_heap_in_terms_of_min_heap)
# print(max_heap_in_terms_of_min_heap)
for i in range(k, len(data_comp)):
    if data[i]<max_heap_in_terms_of_min_heap[0]:
        continue
    heapq.heappushpop(max_heap_in_terms_of_min_heap, data_comp[i])
# print((max_heap_in_terms_of_min_heap[0]*-1))

# data = [4, 5, 3, 2, 1, 6, 4, 3, 8, 9]
# k = 3
# max_heap = data[:k]
# heapq._heapify_max(max_heap)
# print(max_heap)
# for i in range(k, len(data)):
#     if data[i] < max_heap[0]:
#         continue
#     heapq._heappop_max(max_heap)
#     heapq.heappush(max_heap,data[i])
#     heapq._heapify_max(max_heap)
#
# print("vdvdfbgf", max_heap)
