"""
Problem_statement: find the count of a given element in a sorted array
input: [1,2,4,5,5,6,7,8,8,8,8,9], ele = 8
o/p: 4
"""


def solve_left(arr, ele, low, high) -> int:
    mid = int(low + (high - low) / 2)
    if low > high:
        return float('inf')
    if arr[mid] == ele:
        return min(solve_left(arr, ele, low, mid - 1), mid)

    elif arr[mid] > ele:
        return solve_left(arr, ele, low, mid - 1)
    elif arr[mid] < ele:
        return solve_left(arr, ele, mid + 1, high)


def solve_right(arr, ele, low, high) -> int:
    mid = int(low + (high - low) / 2)
    if low > high:
        return -1
    if arr[mid] == ele:
        return max(solve_right(arr, ele, mid + 1, high), mid)

    elif arr[mid] > ele:
        return solve_right(arr, ele, low, mid - 1)
    elif arr[mid] < ele:
        return solve_right(arr, ele, mid + 1, high)


def solve(arr, ele):
    low = 0
    high = len(arr) - 1
    return solve_right(arr, ele, low, high) - solve_left(arr, ele, low, high) + 1


if __name__ == '__main__':
    arr_input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9, 9, 9, 9, 9, 9]
    arr_input_2 = []
    ele_2 = 8
    ele = 9
    print("case1", solve(arr_input, ele))
    print("case2", solve(arr_input_2, ele_2))
