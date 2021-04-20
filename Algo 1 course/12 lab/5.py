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
    answer[u]=max(1+grandchild_sum, child_sum)
    return answer[u]


n=int(input())
n+=1
child = [[] for i in range(n)]
grandchild = [[] for i in range(n)]
answer = [0]*n
start=0
for i in range(1,n):
    a=int(input())
    child[a].append(i)
    if not a:
        start=i

for i in range(n):
    a=child[i]
    for j in a:
        for z in child[j]:
            grandchild[i].append(z)


print(get_independent_set(start))
