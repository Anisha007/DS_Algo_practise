def solve(s1, s2, len_s1, len_s2, k):
    if len_s1 == 0 or len_s2 == 0:
        return 0
    if k == 0:
        return -1
    op1 = 0
    if s1[len_s1 - 1] == s2[len_s2 - 1]:
        op1 = 1+solve(s1, s2, len_s1 - 1, len_s2 - 1, k)
        # print(op1, s1[len_s1-1])
    op2 = max(solve(s1, s2, len_s1, len_s2 - 1, k), solve(s1, s2, len_s1 - 1, len_s2, k))
    op3 = 1 + solve(s1, s2, len_s1 - 1, len_s2 - 1, k - 1)
    return max(op1, op2, op3)


s1 = [1, 2, 3, 4, 5]
s2 = [5, 3, 1, 4, 2]
print(solve(s2, s1, len(s2), len(s1), 1))
