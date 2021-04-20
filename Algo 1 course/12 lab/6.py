def get_independent_set(u):
    global n,answer
    if answer[u]:
        return answer[u]
    child_sum=0
    grandchild_sum=0
    for i in child[u]:
        child_sum = child_sum + get_independent_set(i)
    for i in grandchild[u]:
        grandchild_sum = grandchild_sum + get_independent_set(i)
        
    answer[u]=max(number[u]+grandchild_sum, child_sum)
    return answer[u]

fin=open("selectw.in")
fout=open("selectw.out", "w")
s=fin.readline().split()
n=int(s[0])
n+=1
child = [[] for i in range(n)]
grandchild = [[] for i in range(n)]
answer = [0]*n
start=0
number = [0]*n
for i in range(1,n):
    s=fin.readline().split()
    a,b=int(s[0]),int(s[1])
    number[i]=b
    child[a].append(i)
    if not a:
        start=i

for i in range(n):
    a=child[i]
    for j in a:
        for z in child[j]:
            grandchild[i].append(z)

print(get_independent_set(start),file=fout)
