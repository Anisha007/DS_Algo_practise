s1 = "abmmmnnncd"
s2 = "abedfhf"


def longest_common_subsequence_recursion(s1, s2, n, m):
    if n == 0 or m == 0:
        return 0
    if s1[n - 1] == s2[m - 1]:
        return 1 + longest_common_subsequence_recursion(s1, s2, n - 1, m - 1)
    else:
        return max(longest_common_subsequence_recursion(s1, s2, n, m - 1),
                   longest_common_subsequence_recursion(s1, s2, n - 1, m))


print(longest_common_subsequence_recursion(s1, s2, len(s1), len(s2)))


def longest_common_subsequence_tabularization(s1, s2, n, m):
    dp_table = [[-1 for j in range(m + 1)] for i in range(n + 1)]
    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0 or j == 0:
                dp_table[i][j] = 0
                continue
            if s1[i - 1] == s2[j - 1]:
                dp_table[i][j] = 1 + dp_table[i-1][j-1]
            else:
                dp_table[i][j] = max(dp_table[i][j-1], dp_table[i-1][j])
    return dp_table[n][m]

print(longest_common_subsequence_tabularization(s1, s2, len(s1), len(s2)))