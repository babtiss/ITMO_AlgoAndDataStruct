f=open('height.in', 'r')
t=open('height.out','w')

n=int(f.readline())
mas=[1 for i in range(n)]
answer=1
if n:
    
    for i in range(n-1):
        d=f.readline().split()
        a,l,r=int(d[0]),int(d[1]),int(d[2])
        if l!=0:
            l-=1
            mas[l]=mas[i]+1
            answer = max(answer, mas[l])
        if r!=0:
            r-=1
            mas[r]=mas[i]+1
            answer = max(answer, mas[r])
    print(answer, file =t )

else:
    print(0,file = t)
    

t.close()
