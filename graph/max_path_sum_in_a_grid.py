"""
Given a m-by-n grid: every element is non-negative integer.

Constrains:
(1) a path only contain non-zero cells
(2) a path can extend to 4 directions: up, down, left, right
(3) no same cell in a path
Assumption
(4) cells with non-0 number will not form a cycle

Find the maximum path sum.

                        Input:
                        5 4 1 0
                        1 0 1 2
                        3 0 0 4
                        0 1 2 0
                        1 0 0 0

Output: 21
Explanation: 3 -> 1 -> 5 -> 4 -> 1 -> 1 -> 2 -> 4
"""

from typing import List


def solve_dfs(source, graph, visited):
    if visited[source] != 0:
        return
    visited[source] = 1
    for neighbour in graph[source]:
        solve_dfs(neighbour, graph, visited)
    visited[source] = 2
    return


def solve(m, n, graph, visited, dp_table):
    if m == -1 or m == len(graph) or n == -1 or n == len(graph[0]) or graph[m][n] == 0:
        return 0
    if visited[m][n] == 2:
        return dp_table[m][n]
    if visited[m][n] == 1:
        return 0
    visited[m][n] = 1
    left = solve(m, n - 1, graph, visited, dp_table)
    right = solve(m, n + 1, graph, visited, dp_table)
    top = solve(m - 1, n, graph, visited, dp_table)
    down = solve(m + 1, n, graph, visited, dp_table)
    max_arr = sorted([left, right, top, down], reverse=True)
    dp_table[m][n] = max_arr[0] + max_arr[1] + graph[m][n]
    visited[m][n] = 2
    return dp_table[m][n]


"""
print result and result_path #backtracking
"""


def solve_2(m, n, graph, visited, dp_table):
    if m == -1 or m == len(graph) or n == -1 or n == len(graph[0]) or graph[m][n] == 0:
        return (0,())
    if visited[m][n] == 2:
        return dp_table[m][n]
    if visited[m][n] == 1:
        return (0,())
    visited[m][n] = 1
    left = solve_2(m, n - 1, graph, visited, dp_table)
    right = solve_2(m, n + 1, graph, visited, dp_table)
    top = solve_2(m - 1, n, graph, visited, dp_table)
    down = solve_2(m + 1, n, graph, visited, dp_table)
    max_arr_unsorted = [left, right, top, down]
    max_arr = sorted(max_arr_unsorted, key = lambda x:x[0], reverse=True)
    print(m,n, " p0 ", max_arr)
    dp_table[m][n] = (max_arr[0][0] + max_arr[1][0] + graph[m][n], (*max_arr[1][1][::-1], graph[m][n], *max_arr[0][1]))
    visited[m][n] = 2
    print(m,n,dp_table[m][n])
    return dp_table[m][n]


if __name__ == '__main__':
    arr_input = [[5, 4, 1, 0], [1, 0, 1, 2], [3, 0, 0, 4], [0, 1, 2, 0], [1, 0, 0, 0]]
    m = len(arr_input)
    n = len(arr_input[0])
    visited = [[0 for j in range(n)] for i in range(m)]
    dp_table = [[(0,[]) for j in range(n)] for i in range(m)]
    global_max = [float('-inf'), []]
    for i in range(m):
        for j in range(n):
            if visited[i][j] == 0:
                local_max = solve_2(i, j, arr_input, visited, dp_table)
                # print(i,j,local_max)
                if local_max[0] > global_max[0]:
                    global_max = local_max
    print(global_max)
