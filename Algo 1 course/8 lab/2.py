f=open('input.txt', 'r')
t=open('output.txt','w')
s=f.readline().split()
n=int(s[0])
l=[]
for i in range(n):
    s=f.readline().split()
    l.append(s)
flag=True

for i in range(n):
    if l[i][i]=='1':
        flag=False
    for j in range(i):
        if l[i][j]!=l[j][i]:
            flag=False
        
if flag:
    print('YES',file = t)
else:
    print('NO', file = t)

t.close()
