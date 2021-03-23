''' Считаем число "входящих" и "выходящих" дуг'''

f=open('input.txt', 'r')
t=open('output.txt','w')
s=f.readline().split()
n,m=int(s[0]),int(s[1])
l=[[0]*n for i in range(n)]
for i in range(m):
    s=f.readline().split()
    a,b=int(s[0])-1,int(s[1])-1
    l[a][b]=1
    l[b][a]=1
d=[]
for i in l:
    d.append(sum(i))
print(*d,file=t)
t.close()
