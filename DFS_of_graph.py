visited=set()
def DFS(visited,graph,node):
    if node  not in visited:
        print(node)
        visited.add(node)
        for neighbour  in graph[node]:
            DFS(visited,graph,neighbour)
graph={
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
    }
DFS(visited, graph, 'A')    
