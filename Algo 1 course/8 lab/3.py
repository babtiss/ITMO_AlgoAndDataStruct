f=open('input.txt', 'r')
t=open('output.txt','w')
s=f.readline().split()
n,m=int(s[0]),int(s[1])
flag=False
l=[[0 for i in range(n)] for j in range(n)]
for i in range(m):
    s=f.readline().split()
    a,b=int(s[0]),int(s[1])
    a,b=a-1,b-1
    if l[a][b]==1:
        flag=True
    l[a][b]=1


for i in range(n):
    for j in range(n):
        if l[i][j] and l[j][i]:
            flag=True
        
if flag:
    print('YES',file = t)
else:
    print('NO', file = t)

t.close()
