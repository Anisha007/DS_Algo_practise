"""
arr: [1,2,3,4,5,6,7]
sum = 5
op = 3
op2 = [(1,4),(2,3),(5)]
"""
from typing import List


def count_subset_sum(input_set: List[int], sum: int, n: int) -> int:
    if sum == 0:
        return 1
    if n == 0:
        return 0
    if input_set[n - 1] <= sum:
        return count_subset_sum(input_set, sum - input_set[n - 1], n - 1) + count_subset_sum(input_set, sum, n - 1)
    else:
        return count_subset_sum(input_set, sum, n - 1)


def print_subset(input_set: List[int], sum: int, n: int) -> List[List[int]]:
    if sum == 0:
        return [()]
    if n == 0:
        return []
    if input_set[n - 1] <= sum:

        num_take = print_subset(input_set, sum - input_set[n - 1], n - 1)
        op_take = [(*t, input_set[n - 1]) for t in num_take]
        num_no_take = print_subset(input_set, sum, n - 1)
        op_take.extend(num_no_take)
        return op_take
    else:
        return print_subset(input_set, sum, n - 1)


def set_bit(num, k):
    return num | (1 << k)


def print_subset_bit_manipulation(input_set: List[int], sum: int, n: int) -> List[int]:
    if sum == 0:
        return [0]
    if n == 0:
        return []
    if input_set[n - 1] <= sum:
        num_take = print_subset_bit_manipulation(input_set, sum - input_set[n - 1], n - 1)
        op_take = [set_bit(ele, n - 1) for ele in num_take]
        num_no_take = print_subset_bit_manipulation(input_set, sum, n - 1)
        op_take.extend(num_no_take)
        return op_take
    else:
        return print_subset_bit_manipulation(input_set, sum, n - 1)


print(print_subset_bit_manipulation([1, 2, 3, 4, 5, 6, 7], 5, 7))
