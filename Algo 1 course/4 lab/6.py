f=open('garland.in', 'r')
t=open('garland.out','w')
mas=f.readline().split()
n=int(mas[0])
A=float(mas[1])
 
h=[0]*(n+1)
h[0]=A
l=0
r=h[0]
last=0
while r-l>0.0000001:
    h[1]=(l+r)/2
    flag=True
    for i in range(2,n):
        h[i]=2*(h[i-1])-h[i-2]+2
        if h[i]<0:
            flag=False
            break
    if flag:
        r=h[1]
        last=h[i]
    else:
        l=h[1]
         
print(round(last,2),file=t)
             
t.close()
