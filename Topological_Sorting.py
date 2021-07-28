graph=[[],[0],[0],[0]]
visited=set()
stack=[]
def Topological(node):
    visited.add(node)
    for x in graph[node]:
        if node not in visited:
            Topological(x)
    stack.append(node)
for x in range(len(graph)):
    if x not in visited:
        Topological(x)
print(stack[::-1])
