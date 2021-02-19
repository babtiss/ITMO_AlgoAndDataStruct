def hashf(key):
    result = 0
    for i in range(len(key)):
        result *= 123
        result += ord(key[i]) -64 + 121
        result %= 1000000121
    result %=1000027
    return result
    
       
          
class HashTable:
    def __init__(self):
        self.size = 1000027
        self.keys = [[] for i in range(self.size)]
 
    def add(self, key, value):
        global last
    
        slot = hashf(key)
        a=len(self.keys[slot])
        for i in range(a):
            if self.keys[slot][i][0] == key:
                self.keys[slot][i][1] = value
                return 
           
       
        self.keys[slot].append([key , value, last, None,])
        
        if last!=None:
            last_slot=hashf(last)
            a=len(self.keys[last_slot])
            for j in range(a):
                if self.keys[last_slot][j][0] == last:
                    self.keys[last_slot][j][3] = key
                    break
        last = key
        return
            
         
    def delete(self, key):
        global last
        slot = hashf(key)
        a=len(self.keys[slot])
      
        for z in range(a):
            if self.keys[slot][z][0] == key:
                pr =self.keys[slot][z][2]
                sl =self.keys[slot][z][3]
                if key == last:
                    last = pr
                    
                self.keys[slot][z] , self.keys[slot][a-1] = self.keys[slot][a-1], self.keys[slot][z]
                self.keys[slot].pop()
                
                f1,f2=0,0
                if pr!=None:
                    slotpr=hashf(pr)
                    b=len(self.keys[slotpr])
                    f1=0
                    for i in range(a):
                        if self.keys[slotpr][i][0] == pr:
                            f1=1
                            break
                if sl!=None:
                    slotsl=hashf(sl)
                    b=len(self.keys[slotsl])
                    f2=0
                    for j in range(a):
                        if self.keys[slotsl][j][0] == sl:
                            f2=1
                            break
                        
                if f1 and f2:
                    self.keys[slotsl][j][2] = pr
                    self.keys[slotpr][i][3] = sl
                elif f1:
                    self.keys[slotpr][i][3] = None
                elif f2:
                    self.keys[slotsl][j][2] = None
                return
        return
    def get(self, key):
        slot = hashf(key)
        for i in self.keys[slot]:
            if i[0]==key:
                return i[1]
        return 'none'
    
    def prev(self, key):
        slot = hashf(key)
      
        for z in self.keys[slot]:
            if z[0] == key:
                pr=z[2]
                if pr==None:
                    return None
                slotf=hashf(pr)
                for k in self.keys[slotf]:
                    if k[0] == pr:
                        return k[1]
                return None
        return None
    
    def nex(self, key):
        slot = hashf(key)
        for z in self.keys[slot]:
            if z[0] == key:
                sl=z[3]
                if sl==None:
                    return None
                slotf=hashf(sl)
                for k in self.keys[slotf]:
                    if k[0] == sl:
                        return k[1]
                return None
        return None

f=open('linkedmap.in', 'r')
w=open('linkedmap.out','w')
 
H = HashTable()
s=f.readline().split()
last = None
while s:
    if s[0] == 'put':
        H.add(s[1],s[2])
    elif s[0]=='delete':
        H.delete(s[1])
    elif s[0]=='prev':
        ans=H.prev(s[1])
        if ans!=None:
            print(ans,file = w)
        else:
            print('none',file =w)
    elif s[0]=='next':
        ans=H.nex(s[1])
        if ans!=None:
            print(ans,file = w)
        else:
            print('none',file = w)
    elif s[0]=='get':
        print(H.get(s[1]),file = w)
    s=f.readline().split()
 
   
 
w.close()
