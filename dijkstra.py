
from collections import defaultdict
import heapq
g = [
    [0, 1, 3],
    [1, 2, 2],
    [0, 2, 9]
]
start = 0

distance=[float('inf')]*3


def Dijkstras_Algorithm(source):
    graph=defaultdict(list)
    distance[source]=0
    for x,y,z in g:
        graph[x].append((z,y))
    stack=[(0,source)]
    visited=set()
    heapq.heapify(stack)
    while stack :
        weight,node=heapq.heappop(stack)
        distance[node]=min(distance[node],weight)
        if node not  in visited:
            visited.add(node)
            for w,c in graph[node]:
                heapq.heappush(stack,(w+weight,c))
            
Dijkstras_Algorithm(start)
print('Shortest distance from the source vertex :',distance)





