graph = {'1': ['4', '2'], '2': ['3', '1', '5', '8', '7'], '3': ['10', '9', '4', '2'], '4': ['1', '3'], '5': ['2', '6', '7', '8'], '6': ['5'], '7': ['2', '5', '8'], '8': ['2', '5', '7'], '9': ['3'], '10': ['3']}

visited = set()

def dfs(visited, graph, node):  
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

print("Depth-First Search")
dfs(visited, graph, '1') 