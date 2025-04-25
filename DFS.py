def dfs(graph, start, path=None):
    if path is None:
        path = []
    path.append(start)
    for nbr in graph[start]:
        if nbr not in path:
            dfs(graph, nbr, path)
    return path

# example usage
g = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': [],
    'E': []
}

result = dfs(g, 'A')
print(" -> ".join(result))   # Output: A -> B -> D -> C -> E