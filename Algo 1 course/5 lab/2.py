
 
f=open('check.in', 'r')
t=open('check.out','w')
n=int(f.readline())
if n:
    d=[0]*n
    mas=[[0,0,0] for i in range(n)]
    for i in range(n):
        d=f.readline().split()
        a,le,ri=int(d[0]),int(d[1]),int(d[2])
        le-=1
        ri-=1
        mas[i][0]=a
        mas[i][1]=le
        mas[i][2]=ri
       
    flag = 1
    dl=[[0,10000000000,-10000000000]]
    while dl and flag:
        pars=dl.pop()
        num=pars[0]
        ap=pars[1]
        al=pars[2]
        a,le,ri = mas[num][0],mas[num][1],mas[num][2]
       
        if a>=ap or a<=al:
            flag=0
            break

        if le!=-1:
            if mas[le][0] >= mas[num][0]:
                flag=0
                break
            dl.append([le,a,al])
        if ri!=-1:
            
            if mas[ri][0] <= mas[num][0]:
                flag=0
                break
            dl.append([ri,ap,a])
              
    if flag:
        print('YES',file = t)
    else:
        print('NO',file = t)
else:
    print('YES',file = t)
t.close()
