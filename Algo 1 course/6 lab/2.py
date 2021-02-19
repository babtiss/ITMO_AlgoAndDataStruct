def hashf(key):
    result = 0
    for i in range(len(key)):
        result *= 47
        result += ord(key[i]) -96
        result %= 1000000411
    result %=1000029
    return result
    
       
          
class HashTable:
    def __init__(self):
        self.size = 1000029
        self.keys = [[] for i in range(self.size)]
 
    def add(self, key, value):
        slot = hashf(key)
        a=len(self.keys[slot])
        for i in range(a):
            if self.keys[slot][i][0] == key:
             
                self.keys[slot][i][1] = value
                return 
           
       
        self.keys[slot].append([key , value])
         
    def delete(self, key):
        slot = hashf(key)
        a=len(self.keys[slot])
        for i in range(a):
            if self.keys[slot][i][0] == key:
                self.keys[slot][i] , self.keys[slot][a-1] = self.keys[slot][a-1], self.keys[slot][i]
                self.keys[slot].pop()
                return
        return
    def get(self, key):
        slot = hashf(key)
        for i in self.keys[slot]:
            if i[0]==key:
                return i[1]
        return 'none'

f=open('map.in', 'r')
w=open('map.out','w')
 
H = HashTable()
s=f.readline().split()
while s:

    if s[0] == 'put':
        H.add(s[1],s[2])
    elif s[0]=='delete':
        H.delete(s[1])
    else:
        print(H.get(s[1]),file = w)
        
    s=f.readline().split()
 
   
 
w.close()
