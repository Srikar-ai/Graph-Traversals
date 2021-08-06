graph={0:[2,3],1:[0],2:[1],3:[4],4:[]}
v=5
time=0
def Targans(node):
    global time
    disc[node]=time
    low[node]=time
    time+=1
    stack_check[node]=True
    stack.append(node)
    for v in graph[node]:
        if disc[v]==-1:
            Targans(v)
            low[node]=min(low[node],low[v])
        elif stack_check[v]==True:
            low[node]=min(low[node],disc[v])
    check=-1
    if low[node]==disc[node]:
        print('Component: ',end='')
        while check!=node:
            check=stack.pop()
            print(check,end=' ')
            stack_check[check]=False
        print(' ')

    
disc=[-1]*v
low=[-1]*v
stack_check=[False]*v
stack=[]
for x in range(v):
    if disc[x]==-1:
        Targans(x)

