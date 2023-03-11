"""
DFS or depth first search is a graph traversal algorithm wherein the node which is considered,
all the corresponding
"""


def dfs(graph, visited, node):
    if not node:
        return
    if not visited[node]:
        print(node)
        visited[node] = True
        for child in graph[node.val]:
            dfs(graph, visited, child)


