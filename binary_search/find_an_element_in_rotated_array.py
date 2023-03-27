"""
Given an sorted rotated array, find the element
eg: [6,1,2,3,4,5]
[6,7,8,9,10,11,12,1,2,3,4,5]
find if element a)4 , b)2 is present or not
"""


def pos_min(arr, low, high) -> int:
    if low > high:
        return -1
    mid = int(low + (high - low) / 2)
    n = len(arr)
    if arr[mid] > arr[(mid + 1) % n] and arr[mid] > arr[(mid - 1 + n) % n]:
        return mid
    elif arr[mid] > arr[low] and arr[mid] > arr[high]:
        return pos_min(arr, mid + 1, high)
    elif arr[mid] < arr[low] and arr[mid] < arr[high]:
        return pos_min(arr, low, mid - 1)
    else:
        return pos_min(arr, low, mid - 1)


def binary_search(arr, low, high, ele) -> bool:
    if low > high:
        return False
    mid = int(low + (high - low) / 2)
    if arr[mid] == ele:
        return True
    elif arr[mid] > ele:
        return binary_search(arr, low, mid - 1, ele)
    else:
        return binary_search(arr, mid + 1, high, ele)


def solve(arr, ele) -> bool:
    if not arr:
        return False
    low = 0
    high = len(arr) - 1
    pos = pos_min(arr, low, high)
    print(pos)
    return binary_search(arr[:pos], low, pos - 2, ele) or binary_search(arr[pos:], pos, high, ele)


if __name__ == '__main__':
    arr_input = [6, 7, 8, 10, 11, 12, 1, 2, 3, 4, 5]
    find = 3
    find_2 = 9
    print("case1:", solve(arr_input, find))
    print("case2:", solve(arr_input, find_2))
