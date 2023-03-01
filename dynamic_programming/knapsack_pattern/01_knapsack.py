def knapsack_01(val, weight, capacity):
    n = len(val)
    if n == 0 or capacity == 0:
        return 0
    if weight[n - 1] <= capacity:
        return max(val[n - 1] + knapsack_01(val[:-1], weight[:-1], capacity - weight[n - 1]),
                   knapsack_01(val[:-1], weight[:-1], capacity))
    else:
        return knapsack_01(val[:-1], weight[:-1], capacity)


def knapsack_01_memoization(val, weight, capacity, n, dp_table):
    if n == 0 or capacity == 0:
        return 0
    key = str(n) + "_" + str(capacity)
    print(key)
    if key in dp_table.keys():
        print(key, " ", dp_table[key], " is called!!")
        return dp_table[key]
    if weight[n - 1] <= capacity:
        dp_table[key] = max(
            val[n - 1] + knapsack_01_memoization(val, weight, capacity - weight[n - 1], n - 1, dp_table),
            knapsack_01_memoization(val, weight, capacity, n - 1, dp_table))
    else:
        dp_table[key] = knapsack_01_memoization(val, weight, capacity, n - 1, dp_table)
    return dp_table[key]


def knapsack_01_tabularization(val, weight, capacity, n):
    t = [[-1 for i in range(capacity + 1)] for j in range(n + 1)]
    print(len(t))
    for i in range(n + 1):
        for j in range(capacity + 1):
            if i == 0 or j == 0:
                t[i][j] = 0
                continue
            if weight[i-1] <= j:
                t[i][j] = max(val[i - 1] + t[i - 1][j - weight[i - 1]], t[i - 1][j])
            else:
                t[i][j] = t[i - 1][j]
    for line in t:
        print(line)
    return t[n][capacity]


def knapsack_01_v2(val, weight, capacity, n):
    if n == 0 or capacity == 0:
        return 0
    if weight[n - 1] <= capacity:
        return max(val[n - 1] + knapsack_01_v2(val, weight, capacity - weight[n - 1], n - 1),
                   knapsack_01_v2(val, weight, capacity, n - 1))
    else:
        return knapsack_01_v2(val, weight, capacity, n - 1)


val = [60, 100, 120]
weight = [10, 20, 30]
capacity = 50
# dp_table = dict()
print(knapsack_01(val, weight, capacity))
# print(dp_table)
print(knapsack_01_tabularization(val, weight, capacity, len(val)))
