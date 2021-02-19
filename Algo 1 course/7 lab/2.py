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
d=[]
l=[[0]*3 for i in range(n)]
balans=[0]*n
height=[0]*n
g=[]
for i in range(n):
        g=f.readline().split()
        d.append([int(i)-1 for i in g])
   
answer=[]

for i in range(n-1,-1,-1):
        a,b,c=d[i]
        l[i][0],l[i][1],l[i][2]=a,b,c
        left,right=0,0
        if b!=-1:
            left=AVL(b)
        if c!=-1:
            right=AVL(c)
        f=right-left
        balans[i]=f
        if f>1:
            leftA=l[i][1]
            rightA=l[i][2]
            if balans[rightA] == -1:
                leftB,rightB=l[rightA][1],l[rightA][2]
                leftC,rightC=l[leftB][1],l[leftB][2]
                leftW,rightW=l[leftA][1],l[leftA][2]
                a,w,b,c,z,x,y=l[i][0],l[leftA][0],l[rightA][0],l[leftB][0],l[rightB][0],l[leftC][0],l[rightC][0]
                l[i][0],l[leftA][0],l[rightA][0],l[leftW][0],l[rightW][0],l[leftB][0],l[rightB][0]=c,a,b,w,x,y,z
                print(leftB,leftW,rightB)

            else:
                print('hohotesik')
               
            break
        
print(n)
for i in l:
    for j in i:
        print(j+1,end=' ')
    print()
t.close()
