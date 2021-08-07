V=5
visited=set()
graph=[[1,2,3],[0,2],[0,1],[0,4],[3]]   
discovery=[float('inf')]*V
low_link_value=[float('inf')]*V
parent=[-1 for x in range(V)]
time=0
def Find_Bridges(u):
    global time
    visited.add(u)
    discovery[u]=time
    low_link_value[u]=time
    time+=1
    for v in graph[u]:
        if v not in visited:
            parent[v]=u
            Find_Bridges(v)
            low_link_value[u]=min(low_link_value[u],low_link_value[v])
            if low_link_value[v]>discovery[u]:
                print('There is Bridge :',u,v)
        elif v!=parent[u]:
            low_link_value[u]=min(low_link_value[u],discovery[v])

for x in range(V):
    Find_Bridges(x)
