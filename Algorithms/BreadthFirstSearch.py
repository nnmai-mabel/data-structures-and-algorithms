# BFS algorithm in Python

import collections

# BFS algorithm
def bfs(graph, root):

    visited, queue = set(), collections.deque([root])
    visited.add(root)

    while queue:

        # Dequeue a vertex from queue
        vertex = queue.popleft()
        print(str(vertex) + " ", end="")

        # If not visited, mark it as visited, and
        # enqueue it, because the order to enqueue is
        # the order to visit as well, so can do both at
        # the same time
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


if __name__ == '__main__':
    # graph = {0: [1, 2], 1: [2], 2: [3], 3: [1, 2]}
    # print("Following is Breadth First Traversal: ")
    # bfs(graph, 0)

    graph = {0: [1, 3], 1: [0, 2, 4, 6, 7], 2: [1, 3, 8, 9], 3: [0, 2], 4: [1, 5, 6, 7], 5: [4], 6: [1, 4, 7], 7: [1, 4, 6], 8: [2], 9: [2]}
    print("Following is Breadth First Traversal: ")
    bfs(graph, 0)
