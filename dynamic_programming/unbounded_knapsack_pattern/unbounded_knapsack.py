def knapsack_01_unbounded(val, weight, capacity, n):
    if n == 0 or capacity == 0:
        return 0
    if weight[n - 1] <= capacity:
        return max(val[n - 1] + knapsack_01_unbounded(val, weight, capacity - weight[n - 1], n),
                   knapsack_01_unbounded(val, weight, capacity, n - 1))
    else:
        return knapsack_01_unbounded(val, weight, capacity, n - 1)


val = [60, 100, 120]
weight = [10, 20, 30]
capacity = 50
print(knapsack_01_unbounded(val, weight, capacity, len(val)))
