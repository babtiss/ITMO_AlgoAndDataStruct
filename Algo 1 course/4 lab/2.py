count=0
length = 0
Queue = [0 for i in range(1000001)]
def delete():
    global count
    value = Queue[count]
    count +=1
    return value

def push(a):
    global Queue, length
    Queue[length] = a
    length +=1
    
f=open('queue.in', 'r')
t=open('queue.out','w') 
 

n=int(f.readline())

for i in range(n):
    a=f.readline().split()
    if a[0]=='+':
        push(a[1])
    else:
        print(delete(), file = t)
 
 
t.close()
