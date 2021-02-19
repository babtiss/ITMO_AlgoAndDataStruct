
def push(item):
     global length
     length +=1
     stek[length] = item
          
def delete():
     global length
     a=stek[length]
     length -=1
     return a
          
f=open('postfix.in', 'r')
t=open('postfix.out','w') 
 
stek = [0 for i in range(1000001)]
length = -1
l=f.readline().split()
for i in l:
    if i=='+':
        b=delete()
        a=delete()
        push(a+b)
    elif i=='-':
        b=delete()
        a=delete()
        push(a-b)
    elif i=='*':
        b=delete()
        a=delete()
        push(a*b)
    else:
        push(int(i))
    
print(delete(),file = t)
t.close()
