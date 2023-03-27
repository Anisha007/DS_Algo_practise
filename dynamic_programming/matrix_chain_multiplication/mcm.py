mn = float('inf')
mn1 = float('inf')


def solve(arr, i, j) -> int:
    if i >= j:
        return 0
    global mn
    for k in range(i, j):
        temp_ans = solve(arr, i, k) + solve(arr, k + 1, j) + arr[i - 1] * arr[k] * arr[j]
        if temp_ans < mn:
            mn = temp_ans

    return mn


def solve_memoize(arr, i, j, dp_table):
    global mn1
    if i >= j:
        return 0
    key = str(i)+"_"+str(j)
    if key in dp_table.keys():
        return dp_table[key]
    for k in range(i, j):
        temp_ans = solve_memoize(arr, i, k, dp_table) + solve_memoize(arr, k + 1, j, dp_table) + arr[i - 1] * arr[k] * \
                   arr[j]
        if temp_ans < mn1:
            mn1 = temp_ans
    dp_table[key] = mn1
    return mn1


def mcm(arr):
    if len(arr) < 3:
        return -1

    i = 1
    j = len(arr) - 1
    print(solve(arr, i, j))
    dp_table = dict()
    print(solve_memoize(arr, i, j, dp_table))


arr = [10, 20, 30, 40, 50]
mcm(arr)
