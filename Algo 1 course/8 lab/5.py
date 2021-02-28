def dfs(v):
    global viz,answer
    q=[(v)]
    q2=[]
    c=0
    while q:
        x=q.pop()
        viz[x]=1
        answer[x]=c
        
        for i in l[x]:
            if viz[i]==0:
                viz[i]=1
                q2.append(i)
        if len(q)==0:
            
            q=q2[::]
            c+=1
            q2=[]
        
    
            
f=open('pathbge1.in', 'r')
t=open('pathbge1.out','w')
s=f.readline().split()
n,m=int(s[0]),int(s[1])
l=[[] for i in range(n)]
answer=[0]*n
viz=[0]*n
for i in range(m):
    s=f.readline().split()
    a,b=int(s[0]),int(s[1])
    a,b=a-1,b-1
    l[a].append(b)
    l[b].append(a)

dfs(0)
print(*answer,file = t)
