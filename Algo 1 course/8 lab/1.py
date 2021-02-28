f=open('input.txt', 'r')
t=open('output.txt','w')
s=f.readline().split()
n,m=int(s[0]),int(s[1])
l=[[0 for i in range(n)] for j in range(n)]

for i in range(m):
    s=f.readline().split()
    a,b=int(s[0]),int(s[1])
    a,b=a-1,b-1
    l[a][b]=1
   
    
for i in l:
    print(*i,file = t)

t.close()
