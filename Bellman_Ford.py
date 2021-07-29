v=5
distance=[float('inf')]*v
def BellmanFord(source,v):
    distance[source]=0
    for x in range(v-1):
        for u,v,w in graph:
            if distance[v]>distance[u]+w :
                    distance[v]=distance[u]+w
    for u,v,w in graph:
        if distance[v]>distance[u]+w :
            print('There is a negative cycle ')
            return 
graph=[[0,1,-1],[0,2,4],[1,2,3],[1,3,2],[1,4,2],[3,2,5],[3,1,1],[4,3,-3]]
print(BellmanFord(0,v))
print(distance)

