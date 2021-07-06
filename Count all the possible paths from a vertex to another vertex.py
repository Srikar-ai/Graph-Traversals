l=[]
def Main(u,v):
    visited=[False for x in range(0,6)]
    pathcount=0
    Count(visited,u,v)
    return pathcount
def Count(visited,u,v):   
    visited[u]=True
    if u==v:
        l.append('Found')
    else:
        for i in graph[u]:
            if visited[i]==False:
                Count(visited,i,v)
    visited[u]=False
graph={
    0 : [1],
    1 : [2,3],
    2 : [3,4],
    3 : [],
    4 : [3,5],
    5 : [3]
}
Main(0,3)
print('No of ways we can reach the path from u to v :',len(l))
