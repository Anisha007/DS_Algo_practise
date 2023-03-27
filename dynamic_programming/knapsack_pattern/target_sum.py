"""
target sum is given a sum, you need to find out the no. of ways signs(+, -).
"""


def solve(arr, n, sum_):
    if sum_ == 0:
        return 1
    if n == 0:
        return 0
    if sum_ < arr[n - 1]:
        return solve(arr, n - 1, sum_)
    else:
        return solve(arr, n - 1, sum_) + solve(arr, n - 1, sum_ - arr[n - 1])


def target_sum(arr, sum_):
    s = sum(arr)
    dif = int((s + sum_) / 2)
    if (s + sum_) % 2 != 0:
        return -1
    else:
        return solve(arr, len(arr), dif)


ip_arr = [1, 1, 1, 1, 1]
sum_ = 3
print(target_sum(ip_arr, sum_))
