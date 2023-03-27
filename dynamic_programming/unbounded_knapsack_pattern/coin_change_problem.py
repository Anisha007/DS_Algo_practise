"""
Max no. of ways
"""


def solve(coin, note_val, n):
    if note_val == 0:
        return 1
    if n == 0:
        return 0
    if note_val < coin[n - 1]:
        return solve(coin, note_val, n - 1)
    else:
        op1 = solve(coin, note_val - coin[n - 1], n)
        op2 = solve(coin, note_val, n - 1)
        return op1 + op2


# coin = [2, 3, 5]
# noteval = 10
# print(solve(coin, noteval, len(coin)))


# get the ways
def solve_backtracking(coin, note_val, n):
    if note_val == 0:
        return [()]
    if n == 0:
        return []
    if note_val < coin[n - 1]:
        return solve_backtracking(coin, note_val, n - 1)
    else:
        op1 = solve_backtracking(coin, note_val - coin[n - 1], n)
        op1_res = [(*i, coin[n - 1]) for i in op1]
        op2 = solve_backtracking(coin, note_val, n - 1)
        op1_res.extend(op2)
        return op1_res


coin = [2, 3, 5]
noteval = 10
print(solve_backtracking(coin, noteval, len(coin)))
