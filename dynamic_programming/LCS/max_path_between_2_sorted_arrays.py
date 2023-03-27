"""
s1 = [1,3,5,7,9]
s2 = [1,2,4,5,6,8]
Find the longest path.
A path can be:
1,3,5,7,9 path_sum = 25
1,2,4,5,6,8 path_sum = 26
1,3,5,6,8 path_sum = 23
1,2,4,5,7,9 path_sum = 28
o/p: 28
1,5
"""
from typing import List


def lcs(s1, s2, len_s1, len_s2):
    if len_s1 == 0 or len_s2 == 0:
        return (), ()
    if s1[len_s1 - 1] == s2[len_s2 - 1]:
        op_s1, op_s2 = lcs(s1, s2, len_s1 - 1, len_s2 - 1)
        op_mod_s1 = (*op_s1, len_s1 - 1)
        op_mod_s2 = (*op_s2, len_s2 - 1)
        return op_mod_s1, op_mod_s2
    op1_s1, op1_s2 = lcs(s1, s2, len_s1 - 1, len_s2)
    op2_s1, op2_s2 = lcs(s1, s2, len_s1, len_s2 - 1)
    if len(op1_s1) >= len(op2_s1):
        return op1_s1, op1_s2
    return op2_s1, op2_s2


def solve(s1: List[int], s2: List[int]) -> int:
    op_s1, op_s2 = lcs(s1, s2, len(s1), len(s2))
    i = 0
    j = 0
    res_max = 0
    for e in range(len(op_s1)):
        local_max = max(sum(s1[i:op_s1[e]]), sum(s2[j:op_s2[e]]))
        print(i, op_s1[e], j, op_s2[e])
        print("jdahwkjh",local_max)
        i=op_s1[e]
        j=op_s2[e]
        res_max += local_max
    print(i,j, sum(s1[i:]), sum(s2[j:]))
    res_max+=max(sum(s1[i:]), sum(s2[j:]))
    return res_max


s1 = [2, 3, 5, 6, 7, 9, 20, 21, 22]
s2 = [1, 3, 4, 5, 8, 9, 11, 15, 20, 23]
print(solve(s1, s2))
