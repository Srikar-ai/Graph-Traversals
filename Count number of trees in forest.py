def Main():
    visited=set()
    ans=0
    for x in range(6):
        if x not in visited:
            Dfs(visited,x)
            ans+=1
    return ans

def Dfs(visited,node):
    visited.add(node)
    for x in graph[node]:
        if x not in visited:
            Dfs(visited,x)
    
    
    
graph={
    0 : [1],
    1 : [2,3],
    2 : [3,4],
    3 : [],
    4 : [3,5],
    5 : [3]
}
print('No of trees in forest are :',Main())
