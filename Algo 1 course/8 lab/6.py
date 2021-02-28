def dfs(x,y):
    global n,m
    xend,yend=-1,-1
    q=[(x,y)]
    c=0
    q2=[]
    fl=True
    while q and fl:
        a,b=q.pop()
        
        for xd,yd in ([-1,0],[0,1],[1,0],[0,-1]):
            anew=a+xd
            bnew=b+yd
            if 0<=anew<n and 0<=bnew<m:
                if l[anew][bnew]=='.':
                    l[anew][bnew]=c
                    q2.append([anew,bnew])
                elif l[anew][bnew]=='T':
                    xend,yend=anew,bnew
                    fl=False
                    
            
        if len(q)==0 and fl:
           
            q=q2[::]
            q2=[]
            c+=1
   
    if fl==True:
        print(-1,file = t)
    else:
        ch=c
        answer=''
        while ch!=-1:
        
            ch-=1
            for xd,yd in ([-1,0],[0,1],[1,0],[0,-1]):
                anew=xend+xd
                bnew=yend+yd
                if 0<=anew<n and 0<=bnew<m:
                    if l[anew][bnew]==ch or l[anew][bnew]=='S':
                       
                        xend=anew
                        yend=bnew
                        if xd==-1 and yd==0:
                            answer+='D'
                        elif xd==0 and yd==1:
                            answer+='L'
                        elif xd==1 and yd==0:
                            answer+='U'
                        elif xd==0 and yd==-1:
                            answer+='R'
                        if l[anew][bnew]=='S':
                            ch=-1
                            break
                            
        print(len(answer),file = t)         
        print(answer[::-1],file = t)
 
f=open('input.txt', 'r')
t=open('output.txt','w')
s=f.readline().split()
n,m=int(s[0]),int(s[1])
l=[[0]*m for i in range(n)]
x,y=0,0
for i in range(n):
    s=f.readline()
    for j in range(m):
        l[i][j]=s[j]
        if l[i][j]=='S':
            x,y=i,j

dfs(x,y)
t.close()
