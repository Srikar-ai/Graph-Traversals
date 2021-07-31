# Floyd warshall 
#Time complexity ---> O(V^3)
INF=99999
def All_Pair_Shortest_Path(graph):
    for x in range(len(graph)):
        for y in range(len(graph)):
            for z in range(len(graph)):
                graph[y][z]=min(graph[y][z],graph[y][x]+graph[x][z])
    return graph
graph=[[0, 5, INF, INF],
         [50, 0, 15, 5],
         [30, INF, 0, 15],
         [15, INF, 5, 0]]
print(All_Pair_Shortest_Path(graph))
