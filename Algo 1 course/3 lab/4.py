def pushUp(i):
    
    if i!=0:
    
        if a[(i-1)//2][0] > a[i][0]:
            a[(i-1)//2],a[i] = a[i],a[(i-1)//2]
            pushUp((i-1)//2)
        
def pushDown(i):
    global n
    left = 2*i+1
    right = 2*i+2
    j=0
    if right<n and a[right][0]<a[i][0]:
        j = right
    else:
        j = i
    if left<n and a[left][0]<a[j][0]:
        j=left
    if i!=j:
        a[i],a[j]=a[j],a[i]
        pushDown(j)
        
def extractMin():
    global n
    ans=a[0][0]
    a[0],a[n-1]=a[n-1],a[0]
    n-=1
    pushDown(0)
   
    return ans
        

        
def heap_push(elem,i):
    global n
    n += 1
    a[n-1][0]=elem
    a[n-1][1]=i
    pushUp(n-1)

    
def decrease(x,y):
    for i in range(n):
        if a[i][1]==x:
            break

    a[i][0]=y
    pushUp(i)
   
    


n=0
a=[[0 for i in range(2)] for j in range(1000000)]
f=open('priorityqueue.in', 'r')
s=f.readline().split()

t=open('priorityqueue.out','w')
count = 1
while s:
    if s[0]=='push':
        heap_push(int(s[1]), count)
        
    elif s[0]=='extract-min':
        
        if n==0:
            print('*' , file = t)   
        else:
            print(extractMin() , file = t)
            
    elif s[0]=='decrease-key':
        decrease(int(s[1]),int(s[2]))
    s=f.readline().split()
    count+=1
   
    
t.close()
