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


def knapsack_01_v2(val, weight, capacity, n):
    if n == 0 or capacity == 0:
        return 0
    if weight[n - 1] <= capacity:
        return max(val[n - 1] + knapsack_01_v2(val, weight, capacity - weight[n - 1], n - 1),
                   knapsack_01_v2(val, weight, capacity, n - 1))
    else:
        return knapsack_01_v2(val, weight, capacity, n - 1)


def knapsack_01_tabularization(val, weight, capacity, n):
    t = [[-1 for col in range(capacity + 1)] for row in range(n + 1)]
    print(len(t))
    for i in range(n + 1):
        for j in range(capacity + 1):
            if i == 0 or j == 0:
                t[i][j] = 0
                continue
            if weight[i - 1] <= j:
                t[i][j] = max(val[i - 1] + t[i - 1][j - weight[i - 1]], t[i - 1][j])
            else:
                t[i][j] = t[i - 1][j]
    for line in t:
        print(line)
    return t[n][capacity]


def knapsack_01_space_optimization(val, weight, cap, n):
    t_old = [-1 for i in range(cap + 1)]
    t_new = [-1 for i in range(cap + 1)]
    for i in range(n + 1):
        for j in range(capacity + 1):
            if i == 0 or j == 0:
                t_new[j] = 0
                continue
            if weight[i - 1] <= j:
                t_new[j] = max(val[i - 1] + t_old[j - weight[i - 1]], t_old[j])
            else:
                t_new[j] = t_old[j]
        for e, ele in enumerate(t_new):
            t_old[e] = ele
        # t_old = t_new.copy()
    return t_new[cap]


val = [60, 100, 120]
weight = [10, 20, 30]
capacity = 50
# dp_table = dict()
print(knapsack_01(val, weight, capacity))
# print(dp_table)
print(knapsack_01_space_optimization(val, weight, capacity, len(val)))
