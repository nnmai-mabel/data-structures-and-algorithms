# DFS algorithm in Python

# DFS algorithm
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)

    print(start, end=" ")

    # find the nodes in graph[start] but not in visited
    for next in graph[start] - visited:
        if next not in visited:
            dfs(graph, next, visited)
    return visited

# graph = {'0': set(['1', '2']),
#          '1': set(['0', '3', '4']),
#          '2': set(['0']),
#          '3': set(['1']),
#          '4': set(['2', '3'])}

# dfs(graph, '0')

graph = {0: set([1, 2, 3, 4]),
         1: set([0, 3, 4]),
         2: set([0, 5, 6]),
         3: set([0, 1, 4]),
         4: set([0, 1, 3]),
         5: set([2, 6]),
         6: set([2, 5])}

dfs(graph, 0)