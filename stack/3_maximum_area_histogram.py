"""

"""
from typing import List


def NSL_index_computation(arr: List[int]) -> List[int]:
    res_arr = []
    stack = list()
    psudo_index = -1
    for i in range(len(arr)):
        while len(stack) > 0 and arr[stack[0]] > arr[i]:
            stack.pop(0)
        res_arr.insert(i, psudo_index if len(stack) == 0 else stack[0])
        stack.insert(0, i)
    return res_arr


def NSR_index_computation(arr: List[int]) -> List[int]:
    res_arr = [-1 for i in range(len(arr))]
    stack = list()
    pseudo_index = len(arr)
    for i in range(len(arr) - 1, -1, -1):
        while len(stack) > 0 and arr[stack[0]] >= arr[i]:
            stack.pop(0)
        res_arr[i] = pseudo_index if len(stack) == 0 else stack[0]
        stack.insert(0, i)
    return res_arr


def largestRectangleArea(heights: List[int]) -> int:
    print(heights)
    NSL_index = NSL_index_computation(heights)
    print(heights)
    NSR_index = NSR_index_computation(heights)
    width = []
    area = []
    for i in range(len(heights)):
        width.insert(i, NSR_index[i] - NSL_index[i]-1)
        area.insert(i, heights[i] * width[i])
    print(NSR_index)
    print(NSL_index)
    print(width)
    print(area)
    return max(area)


if __name__ == "__main__":
    input_ = input("Enter the array elements\n")
    input_arr = [int(ele) for ele in input_.split(',')]
    result = largestRectangleArea(input_arr)
    print(result)
