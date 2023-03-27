def solve(source, graph, visited, parent):
    if visited[source] == 2:
        return False
    if visited[source] == 1:
        return True
    visited[source] = 1
    for nbour in graph[source]:
        if solve(nbour, graph, visited, source) and nbour!=parent:
            return True
    visited[source] = 2
    return False
