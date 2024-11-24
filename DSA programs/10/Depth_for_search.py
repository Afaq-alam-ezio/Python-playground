graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}

visited = set()

def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

def depth_first_search(graph, start_node):
    if start_node not in graph:
        print("Start node not found in the graph.")
        return
    print("Following is the Depth-First Search:")
    dfs(visited, graph, start_node)

# Example usage
depth_first_search(graph, '5')
