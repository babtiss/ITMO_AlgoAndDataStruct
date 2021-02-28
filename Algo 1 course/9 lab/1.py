def dfs(v):
    global color,f,answer
    q=[v]
    while q:
        flag=1
        x=q[-1]
        color[x]=1
        for j in l[x]:
            if color[j]==0:
                q.append(j)
                flag=0
                break
            elif color[j]==1:
                f=0
                break
        if flag==1:
            q.pop()
            color[x]=2
            answer.append(x+1)
        
f=open('topsort.in', 'r')
t=open('topsort.out','w')
s=f.readline().split()

n,m=int(s[0]),int(s[1])
l=[[] for i in range(n)]
for i in range(m):
    s=f.readline().split()
    a,b=int(s[0]),int(s[1])
    a,b=a-1,b-1
    l[a].append(b)


answer=[]
color=[0]*n
f=1
for i in range(n):
    if color[i]==0:
        dfs(i)
    
if f==0:
    print(-1,file = t)
else:
    print(*answer[::-1],file = t)
t.close()


                
            
    
    
