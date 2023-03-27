"""
Binary search
"""
from typing import List


def bs_recursive(arr: List[int], ele: int, low: int, high: int) -> bool:
    mid = int((low + high) / 2)
    if low > high:
        return False
    if arr[mid] == ele:
        return True
    elif arr[mid] > ele:
        return bs_recursive(arr, ele, low, mid - 1)
    else:
        return bs_recursive(arr, ele, mid + 1, high)


if __name__ == '__main__':
    input_array = [1, 4, 6, 8, 9, 20, 34, 56, 78, 89]
    ele = 1
    print(bs_recursive(input_array, ele, 0, len(input_array) - 1))
