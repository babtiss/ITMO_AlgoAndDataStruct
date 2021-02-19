
f=open('radixsort.in', 'r')

a=(f.readline().split())
n,length,k=int(a[0]),int(a[1]),int(a[2])
A=[]
for i in range(n):
    s=str(*(f.readline().split()))
    A.append(s)

for i in range(length-1,-1,-1):

    B=dict()
    for t in range(97,123):
        B[chr(t)]=[]
        
    for x in A:
        figure = x[i]
        if figure in B:
            B[figure].append(x)
        else:
            B[figure]=[x]
    
    A=[]
 
    for ki in B:
        for kj in B[ki]:
            A.append(kj)
           
    k-=1
    if k==0:
        break

t=open('radixsort.out','w') 
for z in A:
    print(z , file =t)
t.close()

