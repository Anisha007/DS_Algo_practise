def shortest_common_super_seq(s1, s2, n, m):
    if n == 0:
        return s2[:m]
    if m == 0:
        return s1[:n]
    if s1[n - 1] == s2[m - 1]:
        op1 = shortest_common_super_seq(s1, s2, n - 1, m - 1)
        return op1 + s1[n - 1]
    else:
        op2 = shortest_common_super_seq(s1, s2, n, m - 1)
        op2 = op2 + s2[m - 1]
        op3 = shortest_common_super_seq(s1, s2, n - 1, m)
        op3 = op3 + s1[n - 1]
        if len(op2) > len(op3):
            return op3
        else:
            return op2


s1 = "geek"
s2 = "eke"

print(shortest_common_super_seq(s1, s2, len(s1), len(s2)))
