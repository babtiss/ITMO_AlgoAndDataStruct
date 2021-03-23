'''
Гамильтонов путь существует если можно взять топологически отсортированные вершины, и по итоговому списку пройтись в обратную сторону
ans = abc...def   если можно пройтись a->b->c->...->d->e->f , то гамильтонов путь есть.
'''
def dfs(v):
    global viz,ans
    viz[v]=1
    q=[v]
    while q:
        flag=1
        x=q[-1]
        viz[x]=1
        for j in l[x]:
            if not viz[j]:
                q.append(j)
                flag=0
                break
        if flag==1:
            q.pop()
            ans.append(x)
            
def check(ans):
    for i in range(1,len(ans)):
        flag=True
        v=ans[i]
        for j in range(len(l[v])):
            if l[v][j]==ans[i-1]:
                flag=False
        if flag:
            return False
    return True
            
n,m=map(int,input().split())
l=[[] for i in range(n)]
viz=[0]*n
ans=[]
for i in range(m):
    a,b=map(int,input().split())
    a-=1
    b-=1
    l[a].append(b)
    
for i in range(n):
    if viz[i]==0:
        dfs(i)

if check(ans):
    print('YES')
else:
    print('NO')
