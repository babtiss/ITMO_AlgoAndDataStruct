def dfs(v):
    global color,flag
    q=[(v,1)]
    while q:
       
        x,cv=q.pop()
        color[x]=cv
        for j in l[x]:
            if color[j]==0:
                q.append((j,-cv))
            elif color[j]==cv:
                flag=0
                return
        

          
        
f=open('bipartite.in', 'r')
t=open('bipartite.out','w')
s=f.readline().split()
flag=1
n,m=int(s[0]),int(s[1])
l=[[] for i in range(n)]

for i in range(m):
    s=f.readline().split()
    a,b=int(s[0]),int(s[1])
    if a==b:
        flag=0
    a,b=a-1,b-1
    l[a].append(b)
    l[b].append(a)
    
color=[0]*n
for i in range(n):
    if color[i]==0:
        dfs(i)
 
if flag==0:
    print("NO",file=t)
else:
    print("YES",file=t)
t.close()
