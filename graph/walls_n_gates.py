from typing import List
from collections import deque


def walls_and_gates(grid: List[List[int]]):
    # write your code here
    rows, cols = len(grid), len(grid[0])
    q = deque()
    # visited = [[0 for j in range(cols)] for i in range(rows)]
    dirc = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0:
                q.append((i, j, 0))

    def isValid(i, j):
        if i < 0 or j < 0 or i >= rows or j >= cols or visited[i][j] != 0 or grid[i][j] == -1:
            return False
        return True

    while q:
        i, j, lev = q.popleft()
        # visited[i][j] = 1
        for nr, nc in dirc:
            ni, nj = i + nr, j + nc
            if isValid(ni, nj) and grid[ni][nj] == 2147483647:
                grid[ni][nj] = min(grid[ni][nj], lev + 1)
                q.append((ni, nj, lev + 1))

    return grid


rooms = \
    [[2147483647, -1, 0, 2147483647], [2147483647, 2147483647, 2147483647, -1], [2147483647, -1, 2147483647, -1],
     [0, -1, -1, 2147483647]]
# Output:
# [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
#
# Explanation:
# the 2D grid is:
# INF  -1  0  INF
# INF INF INF  -1
# INF  -1 INF  -1
#   0  -1 INF INF
# the answer is:
#   3  -1   0   1
#   2   2   1  -1
#   1  -1   2  -1
#   0  -1   3   4
print(walls_and_gates(rooms))
