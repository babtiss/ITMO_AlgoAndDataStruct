f=open('quack.in', 'r')
t=open('quack.out','w')
def get():
    global c
    c+=1
    return deq[c]
    
l='a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()
registr=[0]*27
d=dict()
for i in range(len(l)):
    d[l[i]] = i
    
deq=[]
c=-1
s=f.readline()
st=[]
labels=dict()
i=-1
while s:
    i+=1
    if s[0]==':':
        ff=s[1:]
        labels[ff]=i
    st.append(s)
    s=f.readline()
ch=0
while ch<len(st):
    s=st[ch]
    ch+=1
    if s[0]=='>':
        num = d[s[1]]
        a=get()
        registr[num]=a
    elif s[0]=='<':
        num = d[s[1]]
        a = registr[num] 
        deq.append(a)
    elif s[0]=='+':
        a=get()
        b=get()
        deq.append((a+b)%65536)
    elif s[0]=='-':
        a=get()
        b=get()
        deq.append((a-b)%65536)
    elif s[0]=='/':
        a=get()
        b=get()
        deq.append(a//b)
    elif s[0]=='*':
        a=get()
        b=get()
        deq.append((a*b)%65536)
    elif s[0]=='%':
        a=get()
        b=get()
        deq.append(a%b)
    elif s[0]=='P' and len(s)==1:
        print(get(),file = t)
    elif s[0]=='P':
        num=d[s[1]]
        print(registr[num],file = t)
        
    elif s[0]=='C' and len(s)==1: 
        print(get()%256, file = t)
    elif s[0]=='C':      
        num=d[s[1]]
        print(registr[num]%256, file =t )
        
    elif s[0]==':':
        a=a
    elif s[0]=='J':
        a=s[1:]
        ch=labels[a]
    elif s[0]=='Z':
        a=d[s[1]]
        a=registr[a]
        b=s[2:]
        if a==0:
            ch = labels[b]
    elif s[0]=='E':
        num=d[s[1]]
        r1=registr[num]
        num=d[s[2]]
        r2=registr[num]
        b=s[3:]
        if r1==r2:
            ch=labals[b]
    elif s[0]=='G':
        num=d[s[1]]
        r1=registr[num]
        num=d[s[2]]
        r2=registr[num]
        b=s[3:]
        if r1>r2:
            ch=labals[b]
    elif s[0]=='Q':
        break
    else:
        a=int(s)
        deq.append(a)
    
t.close()
