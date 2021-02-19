f=open('binsearch.in', 'r')
t=open('binsearch.out','w') 
n=int(f.readline())
l=f.readline().split()
for i in range(n):
    l[i]=int(l[i])

k=int(f.readline())
g=f.readline().split()

for i in g:
    k=int(i)
    left=0
    right=n
    while left<right:
        mid=(left+right)//2
        if k<l[mid]:
            right=mid
        elif l[mid]==k:
            right=mid
        else:
            left=mid+1

    t1=left
    k +=1
    right=n
    while left<right:
        mid=(left+right)//2
        if k<l[mid]:
            right=mid
        elif l[mid]==k:
            right=mid
        else:
            left=mid+1
    t2=left
   
    if t1>=n:
        print('-1 -1',file=t)
    elif l[t1]!=k-1:
        print('-1 -1',file=t)
    else:
        print(t1+1,t2,file=t)
            
t.close()


    
