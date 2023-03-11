from typing import List


def subset_sum(ele_set: List[int], sum: int, n: int) -> bool:
    if sum==0:
        return True
    if n == 0:
        return False
    if ele_set[n - 1] > sum:
        return subset_sum(ele_set, sum, n - 1)
    elif ele_set[n - 1] <= sum:
        return subset_sum(ele_set, sum - ele_set[n - 1], n - 1) or subset_sum(ele_set, sum, n - 1)


def eq_sum_partition(ele_set: List[int]) -> bool:
    sum_ = sum(ele_set)
    if sum_ % 2 != 0:
        return False
    else:
        return subset_sum(ele_set, int(sum_ / 2), len(ele_set))


print(eq_sum_partition([7, 2, 3, 4, 5, 1]))
