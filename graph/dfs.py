"""
DFS or depth first search is a graph traversal algorithm wherein the node which is considered,
all the corresponding
"""


def dfs(source, graph, visited):
    if visited[source] != 0:
        return []
    visited[source] = 1
    nodelist = []
    for neighbour in graph[source]:
        nodelist.append(dfs(neighbour, graph, visited))
    visited[source] = 2
    nodelist.append(source)
    return nodelist



