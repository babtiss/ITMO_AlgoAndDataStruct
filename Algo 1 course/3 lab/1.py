'''
Основное свойство неубывающей пирамиды: a[i]<=a[2*i] and a[i]<=a[2*i+1] для 1<=i<=n.
'''
f=open('isheap.in', 'r')
n=int(f.readline())
a=(f.readline().split())

l=[0]
for i in range(n):
    l.append(int(a[i]))

fl=1

for i in range(1,n+1):
    if 2*i<=n:
        if l[i]>l[2*i]:
            fl=0
            break
    if 2*i+1<=n:
        if l[i]>l[2*i+1]:
            fl=0
            break
    else:
        break
    
t=open('isheap.out','w') 
if fl:
    print('YES',file=t)
else:
    print('NO',file=t)

t.close()
