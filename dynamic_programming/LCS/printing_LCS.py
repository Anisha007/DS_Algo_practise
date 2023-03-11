"""
Print all possible LCS.
"""

s1 = "fabmncd"
s2 = "fmnabd"
from typing import List


def longest_common_subsequence_recursion(s1, s2, n, m) -> List[str]:
    if n == 0 or m == 0:
        return [""]
    if s1[n - 1] == s2[m - 1]:
        op = longest_common_subsequence_recursion(s1, s2, n - 1, m - 1)
        op_new = [ele + s1[n - 1] for ele in op]
        return op_new
    else:
        op1 = longest_common_subsequence_recursion(s1, s2, n, m - 1)
        op2 = longest_common_subsequence_recursion(s1, s2, n - 1, m)
        if len(op1[0]) == len(op2[0]):
            op1.extend(op2)
            return op1
        res = op1 if len(op1[0]) > len(op2[0]) else op2
        return res


res = longest_common_subsequence_recursion(s1, s2, len(s1), len(s2))
# res = set(res)
print(res)

dp_table = dict()


def print_lcs_tabularization_dict(s1, s2, n, m, dp_table):
    key = str(n)+"_"+str(m)
    if n == 0 or m == 0:
        return [""]
    if key in dp_table.keys():
        return dp_table[key]

    if s1[n - 1] == s2[m - 1]:
        op = print_lcs_tabularization_dict(s1, s2, n - 1, m - 1, dp_table)
        op_new = tuple(ele + s1[n - 1] for ele in op)
        dp_table[key] = op_new
        return op_new
    else:
        op1 = print_lcs_tabularization_dict(s1, s2, n, m - 1, dp_table)
        op2 = print_lcs_tabularization_dict(s1, s2, n - 1, m, dp_table)
        if len(op1[0]) == len(op2[0]):
            op =(*op1, *op2)
            dp_table[key] = op
            return op
        res = op1 if len(op1[0]) > len(op2[0]) else op2
        dp_table[key] = res
        return res


def print_longest_common_subsequence_tabularization(s1, s2, n, m):
    dp_table = [[-1 for j in range(m + 1)] for i in range(n + 1)]
    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0 or j == 0:
                dp_table[i][j] = 0
                continue
            if s1[i - 1] == s2[j - 1]:
                dp_table[i][j] = 1 + dp_table[i - 1][j - 1]
            else:
                dp_table[i][j] = max(dp_table[i][j - 1], dp_table[i - 1][j])
    # print(dp_table)
    [print(line) for line in dp_table]


    return dp_table[n][m]


print(print_lcs_tabularization_dict(s1, s2, len(s1), len(s2), dp_table))
print(print_longest_common_subsequence_tabularization(s1, s2, len(s1), len(s2)))


