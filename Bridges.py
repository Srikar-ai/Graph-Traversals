V=5
graph=[[1,2,3],[0,2],[0,1],[0,4],[3]]
visited=set()
disc=[float('inf')]*V
low=[float('inf')]*V
parent=[-1 for x in range(V)]
time=0
def dfs(node):
    global time
    visited.add(node)
    disc[node]=time
    low[node]=time
    time+=1
    for x in graph[node]:
        if x not in visited:
            parent[x]=node
            dfs(x)
            low[node]=min(low[node],low[x])
            if low[x]>disc[node]:
                print('bridge...',x,node)
        elif x!=parent[node]:
            low[node]=min(low[node],disc[x])



for x in range(V):
    dfs(x)
print(parent)
