def bfs():
    global flag
    q=[]
    for i in range(n):
        if len(l[i])==0:
            q.append(i)
            color[i]=-1
    mn=[]

    while q:
        x=q.pop()
        for i in l_inv[x]:
            if color[i]==0:
                color[i]=-color[x]
                mn.append(i)
            elif color[i]==-1 and color[x]==-1:
                color[i]=1
                mn.append(i)
        if len(q)==0:
            q=mn[:]
            mn=[]
   
n,m,s=map(int,input().split())
l=[[] for i in range(n)]
l_inv=[[] for i in range(n)]
color=[0]*n
flag=0
for i in range(m):
    a,b=map(int,input().split())
    a,b=a-1,b-1
    l[a].append(b)
    l_inv[b].append(a)


bfs()
if color[s-1]==1:
    print('First player wins')
else:
    print('Second player wins')
