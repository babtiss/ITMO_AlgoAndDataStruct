'''
push (запись в стек) — операция вставки нового элемента. O(1)
delete (снятие со стека) — операция удаления нового элемента. O(1)
Для стека с n элементами требуется O(n) памяти, так как она нужна лишь для хранения самих элементов.
'''
class Stack:
    def __init__(self):
        self.values = []

    def push(self, item):
        self.values.append(item)

    def delete(self):
        if self.values:
            return self.values.pop()
        return None
def main()          
     f=open('stack.in', 'r')
     t=open('stack.out','w') 

     n=int(f.readline())
     for i in range(n):
         a=f.readline().split()
         if a[0]=='+':
             push(a[1])
         else:
             print(delete(), file = t)
     t.close()
main()
