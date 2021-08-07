V=5
graph=[[1,2,3],[0,2],[0,1],[0,4],[3]]
#visited to check the node is visited
visited=set()
#discovery time 
discovery=[float('inf')]*V
#low link values
low_link_values=[float('inf')]*V
#parent of each node
parent=[-1 for x in range(V)]
#articulation point 
articulation=[False]*V
#initial time=0
time=0
def Find_Articulation_Point(u):
    global time
    c=0
    visited.add(u)
    discovery[u]=time
    low_link_values[u]=time
    time+=1
    for v in graph[u]:
        if v not in visited:
            parent[v]=u
            c+=1
            Find_Articulation_Point(v)
            if parent[u]==-1 and c>1:
                articulation[u]=True
            elif parent[u]!=-1 and low_link_values[v]>=discovery[u]:
                articulation[u]=True
        low_link_values[u]=min(low_link_values[u],discovery[v])
for x in range(V):
    Find_Articulation_Point(x)
print(articulation)

