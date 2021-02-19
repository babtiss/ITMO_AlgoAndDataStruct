class Node:
    def __init__(self, data ):

        self.left = None
        self.right = None
        self.data = data
        self.parent = None
            
    def findval(self, lkpval):
        if lkpval < self.data:
            if self.left == None:
                return 'false'
            return self.left.findval(lkpval)
        elif lkpval > self.data:
            if self.right == None:
                return 'false'
            return self.right.findval(lkpval)
        else:
            return 'true'
          
        
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

def delete(root,z):                      
    if root==None:
        return root
    if z<root.data:
        root.left=delete(root.left,z)
    elif z>root.data:
        root.right=delete(root.right,z)
        
    elif root.left!=None and root.right !=None:
        root.data= minimum(root.right).data
        root.right=delete(root.right, root.data)
    else:
        if root.left !=None:
            root=root.left
        elif root.right !=None:
            root=root.right
        else:
            root=None
    return root


def next(root,x):
    successor = None
    while root!=None:
        if root.data > x:
            successor = root
            root = root.left
        else:
            root = root.right
    if successor == None:
        return 100000000000000000
    else:
        return successor.data
    
def prev(root,x):
    successor = None
    while root!=None:
        if root.data >= x:
            root = root.left
        elif root.data < x:
            successor = root
            root = root.right
    if successor == None:
        return 100000000000000000
    else:
        return successor.data
    
f=open('bstsimple.in', 'r')
t=open('bstsimple.out','w')
s=f.readline().split()
root = Node(100000000000000000)
while s:
    if s[0]=='insert':
        insert(root, (int(s[1])))
        
    elif s[0]=='exists':
        a=root.findval(int(s[1]))
        print(a,file = t)
        
    elif s[0]=='delete':
        root = delete(root, int(s[1]))

    elif s[0]=='prev':
        a=prev(root,int(s[1]))
        if a==100000000000000000:
            print('none',file = t)
        else:
            print(a,file = t)
            
    elif s[0]=='next':
        a=next(root,int(s[1]))
        if a==100000000000000000:
            print('none',file = t)
        else:
            print(a,file = t)

    s=f.readline().split()

t.close()
