def dfs(vertex,visited,graph):
    visited.add(vertex)
    for x in graph[vertex]:
        if x not in visited:
            dfs(x,visited,graph)
def FindMother(graph):
    m=0
    visited=set()
    for x in range(1,6+1):
        if x not in visited:
            dfs(x,visited,graph)
            m=x
    print(m)

graph={
    1 : [2],
    2 : [3,4],
    3 : [5],
    4 : [],
    5 : [6],
    6 : []
    }
FindMother(graph)
