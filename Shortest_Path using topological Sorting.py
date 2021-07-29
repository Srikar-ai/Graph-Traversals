graph={0: [(1, 5), (2, 3)], 1: [(3, 6), (2, 2)], 2: [(4, 4), (5, 2), (3, 7)], 3: [(4, -1)], 4: [(5, -2)]}
V=6
visited=set()
stack=[]
def TopologicalSort(node):
    visited.add(node)
    if node in graph.keys():
        for x,y in graph[node]:
            if x not in visited:
                TopologicalSort(x)
    stack.append(node)

def ShortestPath(source):
    for x in range(V):
        if x not in visited:
            TopologicalSort(x)
    distance=[float('inf')]*V
    distance[source]=0
    while stack:
        k=stack.pop()
        if k in graph.keys():
            for n,w in graph[k]:
                if distance[n]>distance[k]+w:
                    distance[n]=distance[k]+w
    print(distance)

ShortestPath(1)




