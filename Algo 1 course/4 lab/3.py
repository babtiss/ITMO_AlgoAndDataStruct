
def push(item):
     global lengthS
     lengthS +=1
     stek[lengthS] = item
          
def delete():
     global lengthS
     a=stek[lengthS]
     lengthS -=1
     return a

          
f=open('brackets.in', 'r')
t=open('brackets.out','w') 
lengthS = -1
stek = [0 for i in range(1000001)]
length=0
a=f.readline().split()

flag=1
while a:
    a=a[0]
    flag=1
    length=0
  
    for i in a:
        if i=='(' or i=='[':
            push(i)
            length+=1
        elif length!=0:
            
            sim = delete()
            length -= 1
            
            if i==')':
                if sim=='(':
                    flag=flag
                else:
                    flag=0
                    break
            elif i==']':
                if sim=='[':
                    flag=flag
                else:
                    flag=0
                    break
        else:
            flag=0
            break
                
    if flag and length==0:
        print('YES', file=t)
    else:
        print('NO', file=t)

    a=f.readline().split()
    
t.close()
