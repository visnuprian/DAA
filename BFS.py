import collections

def bfs(graph, root):

    visited, queue = set(), collections.deque([root])
    visited.add(root)

    while queue:

        vertex = queue.popleft()
        print(str(vertex) + " ", end="")

        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

if __name__ == '__main__':
    graph = {1: [4, 2], 2: [3, 1, 5, 8, 7], 3: [10, 9, 4, 2], 4: [1, 3], 5: [2, 6, 7, 8], 6: [5], 7: [2, 5, 8], 8: [2, 5, 7], 9: [3], 10: [3]}
    print("Breadth First Traversal is: ")
    bfs(graph, 6)