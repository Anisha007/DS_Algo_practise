"""
k_closest_number
"""
from typing import List
import heapq


def solve(nums: List[int], k: int, n: int) -> List[int]:
    heap_ds = []
    res = []
    nums_mod = [(-1) * abs(nums[i] - n) for i in range(len(nums))]
    print(nums_mod)
    for (i, ele) in enumerate(nums_mod[:k]):
        print(i)
        heap_ds.append((ele, i))  # here we are pushing the items in pair in heap
    heapq.heapify(heap_ds)
    print("heap ds = ", heap_ds)
    for (i, ele) in enumerate(nums_mod[k:]):
        if ele < heap_ds[0][0]:
            continue
        heapq.heappushpop(heap_ds, (ele, i))
    print("modified heap = ", heap_ds)
    for (ele, i) in heap_ds:
        res.append(nums[i])
    return res


print(solve([2, 5, 7, 9, 8, 6, 4, 2, 1], 3, 5))
