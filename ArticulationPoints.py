V=5
graph=[[1,2,3],[0,2],[0,1],[0,4],[3]]
visited=set()
disc=[float('inf')]*V
low=[float('inf')]*V
parent=[-1 for x in range(V)]
ap=[False]*V
time=0
def dfs(node):
    children=0
    global time
    visited.add(node)
    disc[node]=time
    low[node]=time
    time+=1
    for x in graph[node]:
        if x not in visited:
            parent[x]=node
            children+=1
            dfs(x)
            if  parent[node]==-1 and children>1:
                ap[node]=True
            if parent[node]!=-1 and low[x]>=disc[node]:
                ap[node]=True
        elif x!=parent[node]:
            low[node]=min(low[node],disc[x])



for x in range(V):
    dfs(x)
print(ap)
