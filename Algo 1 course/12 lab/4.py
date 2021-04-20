fin=open("knight2.in")
fout=open("knight2.out", "w")
s=fin.readline().split()
a,b=int(s[0]),int(s[1])
l=[[0]*b for i in range(a)]
x=0
y=0
l[0][0]=1
for i in range(a):
            x,y=i,0
       
            while 0<=x and 0<=y<b:
                t=0
                for xd,yd in ([1,-2],[-1,-2],[-2,-1],[-2,1]):
                    if 0<=x+xd<a and 0<=y+yd<b and l[x+xd][y+yd]>0:
                        t +=l[x+xd][y+yd]
                l[x][y] +=t
                x=x-1
                y=y+1
                
for j in range(1,b):
            x,y=a-1,j
            while 0<=x and y<b:
                t=0
                for xd,yd in ([1,-2],[-1,-2],[-2,-1],[-2,1]):
                    if 0<=x+xd<a and 0<=y+yd<b:
                        t +=l[x+xd][y+yd]
                l[x][y] +=t
                x=x-1
                y=y+1
                
print(l[a-1][b-1],file=fout)
fout.close()
