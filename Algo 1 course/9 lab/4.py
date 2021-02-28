def dfs1(v):
    global color,f
    q=[v]
    while q:
     
        flag=1
        x=q[-1]
        color[x]=1
        for j in l[x]:
            if not color[j]:
                q.append(j)
                flag=0
                break
        if flag==1:
            q.pop()
            f.append(x)
            
     
def dfs2(v):
    global component
    
    q=[v]
    while q:
        x=q.pop()
        component[x]=col
        for j in l_inv[x]:
            if not component[j]:
                q.append(j)
                
fp=open('cond.in', 'r')
t=open('cond.out','w')
s=fp.readline().split()

n,m=int(s[0]),int(s[1])
 
l=[[] for i in range(n)]
l_inv=[[] for i in range(n)]
f=[]
color=[0]*n
component=[0]*n
 
for i in range(m):
    s=fp.readline().split()
    a,b=int(s[0]),int(s[1])
    a-=1
    b-=1
    l[a].append(b)
    l_inv[b].append(a)
     
for i in range(n):
    if not color[i]:
        dfs1(i)
col=1

for i in f[::-1]:
    if not component[i]:
        dfs2(i)
        col+=1
print(col-1,file = t)
print(*component,file = t)
t.close()
