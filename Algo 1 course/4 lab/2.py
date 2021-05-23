class Queue:
    def __init__(self):
        self.values = []
        self.iterator = 0

    def delete(self):
        self.iterator += 1
        return self.values[self.iterator - 1]

    def push(self, curr):
        self.values.append(curr)

    
f=open('queue.in', 'r')
t=open('queue.out','w') 
 

n=int(f.readline())
q = Queue
for i in range(n):
    a=f.readline().split()
    if a[0]=='+':
        q.push(a[1])
    else:
        print(q.delete(), file = t)
 
 
t.close()
