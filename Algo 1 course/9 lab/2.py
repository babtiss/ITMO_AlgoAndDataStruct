def dfs(v):
    global color,f,answer,d
    q=[v]
    while q:
        stop=1
        x=q[-1]
        for i in l[x]:
            if color[i]==0:
                color[i]=1
                q.append(i)
                stop=0
                break
            elif color[i]==1:
                f=0
                answer.append(i+1)
                color[i]=2
                q.append(i)
                stop=0
                break
        if stop:
            if f==0:
                return
            q.pop()
            color[x]=2
f=open('cycle.in', 'r')
t=open('cycle.out','w')


s=f.readline().split()

n,m=int(s[0]),int(s[1])
l=[[] for i in range(n)]
for i in range(m):
    s=f.readline().split()
    a,b=int(s[0]),int(s[1])
    a,b=a-1,b-1
    if not b in l[a]:
        l[a].append(b)

answer=[]
d=dict()
color=[0]*n
f=1
for i in range(n):
    if color[i]==0 and f==1:
        color[i]=1
        dfs(i)
    
if f==0:
    print('YES',file = t)
    print(*answer,file = t)
else:
    print('NO', file = t)
    
t.close()
