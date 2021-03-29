visited=set() # to check wheather nodes are visited or not
queue=[]#Initialize queue
def BFS(visited,graph,node):
    visited.add(node)
    queue.append(node)
    while queue:
        s=queue.pop(0)
        print(s)
        for neighbour  in graph[s]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


graph={
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
    }

BFS(visited,graph,'A')   
