V=5

graph=[[2,3],[0],[1],[4],[]]   
stack=[]
def DFS(node,visited,graph):
    visited.add(node)
    print(node,end=' ')
    for v in graph[node]:
        if v not in visited:
            DFS(v,visited,graph)
def Reverse():
    rev=[[] for x in range(V)]
    for x in range(V):
        for y in graph[x]:
            rev[y].append(x)
    return rev
def Topological(u,visited):
    visited.add(u)
    for v in graph[u]:
        if v not in visited:
            Topological(v,visited)
    stack.append(u)

def Kosaraju_Algorithm():
    visited=set()
    for x in range(V):
        if x not in visited:
            Topological(x,visited)
    reverse_graph=Reverse()
    visited=set()
    while stack:
        node=stack.pop()
        if node not in visited:
            DFS(node,visited,reverse_graph)
            print("")


Kosaraju_Algorithm()
