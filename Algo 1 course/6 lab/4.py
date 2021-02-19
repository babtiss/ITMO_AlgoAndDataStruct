class Node:
    def __init__(self, data):
  
        self.left = None
        self.right = None
        self.data = data
        self.parent = None
              
    def findval(self, lkpval):
        if lkpval < self.data:
            if self.left == None:
                return False
            return self.left.findval(lkpval)
        elif lkpval > self.data:
            if self.right == None:
                return False
            return self.right.findval(lkpval)
        else:
            return True
         
def travel(x,d):
 
    if x:
        travel(x.left,d)
        travel(x.right,d)
        d.append(x.data)
        return
         
         
         
def minimum(x):
    while x.left!=None:
        x=x.left
    return x
         
      
def maximum(x):
    while x.right!=None:
            x=x.right
    return x
   
def insert(x,z):
        if x==None:
            return Node(z)
        elif z<x.data:
            x.left = insert(x.left,z)
        elif z>x.data:
            x.right = insert(x.right,z)
        return x
  
def deleteTree(root,z):
    
    if root==None:
        return root
    if z<root.data:
        root.left=deleteTree(root.left,z)
    elif z>root.data:
        root.right=deleteTree(root.right,z)
          
    elif root.left!=None and root.right !=None:
        root.data= minimum(root.right).data
        root.right=deleteTree(root.right, root.data)
    else:
        if root.left !=None:
            root=root.left
        elif root.right !=None:
            root=root.right
        else:
            root=None
     
    return root
  
 
 
def hashf(key):
    result = 0
    for i in key:
        x = (ord(i) -96)
        result = (result*7 + x) % 100029
    return result%100029
       
def add(key, value,keys):
        slot = hashf(key)
           
        for i in keys[slot]:
            if i[0] == key :
                insert(i[1],value)
                return
        a=Node('WWWWWWWWWWWWWWWWWWWWWW')
         
        keys[slot].append([key , insert(a,value)])
        return
     
def delete(key, value,keys):
        slot = hashf(key)
        a=len(keys[slot])
        for i in range(a):
            if keys[slot][i][0] == key :
                keys[slot][i][1]=deleteTree(keys[slot][i][1],value)
                return
        return
       
def get(key,keys):
        slot = hashf(key)
        answer=[]
        d=0
        for i in keys[slot]:
            if i[0]==key:
                travel(i[1],answer)
        return len(answer),answer
      
def deleteall(key,keys):
        slot = hashf(key)
        a=len(keys[slot])
        i=0
        while i<a:
            if keys[slot][i][0] == key :
                keys[slot][i] , keys[slot][a-1] = keys[slot][a-1], keys[slot][i]
                keys[slot].pop()
                return
            else:
                i+=1
        return
def main():
    size = 100029
    keys = [[] for i in range(size)]
    f=open('multimap.in', 'r')
    w=open('multimap.out','w')
    for s in f.readlines():
        s=s.split()
        if s[0] == 'put':
            add(s[1],s[2],keys)
        elif s[0]=='delete':
            delete(s[1],s[2],keys)
        elif s[0]=='get':
            a,b = get(s[1],keys)
            if a==0:
                a=1
            print(a-1,end=' ',file = w)
            print(*b[:-1],file = w)
        else:
            deleteall(s[1],keys)
    w.close()
main()
