
def push(item):
     global length
     length +=1
     stek[length] = item
          
def delete():
     global length
     a=stek[length]
     length -=1
     return a
          
f=open('stack.in', 'r')
t=open('stack.out','w') 
 
stek = [0 for i in range(1000001)]
length = -1
n=int(f.readline())
for i in range(n):
    a=f.readline().split()
    if a[0]=='+':
        push(a[1])
    else:
        print(delete(), file = t)
 
 
t.close()
