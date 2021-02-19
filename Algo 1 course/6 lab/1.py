def hashf(key):
    return (key +234567) % 1000029

def add(key,keys):
    slot = hashf(key)
    if key in keys[slot]:
        return
    keys[slot].append(key)
         
def delete(key,keys):
    slot = hashf(key)
    a=len(keys[slot])
    for i in range(a):
        if keys[slot][i] == key:
            keys[slot][i] , keys[slot][a-1] = keys[slot][a-1], keys[slot][i]
            keys[slot].pop()
            return
    return

def exists(key,keys):
    slot = hashf(key)
    if key in keys[slot]:
            return True
    return False
def main():
        size = 1000029
        keys = [[] for i in range(size)]
        f=open('set.in', 'r')
        w=open('set.out','w')
        for s in f.readlines():
            s=s.split()
            a,b=s[0],int(s[1])
            if a == 'insert':
                add(b,keys)
            elif a=='delete':
                delete(b,keys)
            else:
                if exists(b,keys):
                    print('true',file = w)
                else:
                    print('false',file = w)

        w.close()
main()
