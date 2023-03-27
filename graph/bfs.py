"""
graph is represented using adjacency list
We will write both the implementation of bfs
iterative and recursive
"""

def bfs(source, graph, visited):
    if visited[source]!=0:
        return
    queue = [source]
    visited[source]=1
    while queue:
        v = queue.pop(0)
        for neighbour in graph[v]:
            queue.append(neighbour)
            visited[neighbour]=1

def bfs_recursive(graph, queue, visited):  # here only concept of unvisited and visited so visited array will only have 0 and 1
    if not queue:
        return
    v = queue.popleft()
    for neighbour in graph[v]:
        if not visited[neighbour]:
