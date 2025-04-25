from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        vertex = queue.popleft()

        if vertex not in visited:
            print("->", vertex, end=' ')
            visited.add(vertex)
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)

# Example usage
graph = {
    'A': ['K', 'H', 'P'],
    'K': ['L', 'O', 'R'],
    'H': ['T'],
    'P': ['N', 'M'],
    'N': [],
    'T': [],
    'R': [],
    'L': [],
    'O': [],
    'M': ['J'],
    'J': [],
}

bfs(graph, 'A')
