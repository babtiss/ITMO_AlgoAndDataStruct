import sys
sys.setrecursionlimit(1000000000)
def AVL(v):
    global height
    a,b=l[v][1],l[v][2]
    if height[v]:
        return height[v]
    if a==-1 and b==-1:
        height[v]=1
        return 1
    elif a==-1:
        height[v]=AVL(b)+1
        return height[v]
    elif b==-1:
        height[v]= AVL(a)+1
        return height[v]
    else:
        height[v]=max(AVL(a),AVL(b))+1
        return height[v]
         
 
f=open('balance.in', 'r')
t=open('balance.out','w')
n=int(f.readline())
l=[]
height=[0]*n
for i in range(n):
        d=f.readline().split()
        l.append([int(i)-1 for i in d])
   
answer=[]
for i in range(n-1,-1,-1):
        a,b,c=l[i]
        left,right=0,0
        if b!=-1:
            left=AVL(b)
        if c!=-1:
            right=AVL(c)
        answer.append(right-left)
for i in range(n-1,-1,-1):
    print(answer[i],file = t)
t.close()
