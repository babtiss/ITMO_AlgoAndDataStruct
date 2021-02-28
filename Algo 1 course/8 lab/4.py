def dfs(v,c):
    global viz,color
    q=[(v)]
    viz[v]=1
    while q:
        x=q.pop()
        color[x]=c
        for i in l[x]:
            if not viz[i]:
                viz[i]=1
                q.append(i)
            
 
f=open('components.in', 'r')
t=open('components.out','w')
s=f.readline().split()
n,m=int(s[0]),int(s[1])
l=[[] for i in range(n)]
r=[]
for i in range(m):
    s=f.readline().split()
    a,b=int(s[0]),int(s[1])
    a,b=a-1,b-1
    l[a].append(b)
    l[b].append(a)
    
viz=[0]*n
color=[0]*n
c=0
for i in range(n):
    if not viz[i]:
        c +=1
        dfs(i,c)
       
print(c, file = t)
print(*color, file = t)

t.close()
