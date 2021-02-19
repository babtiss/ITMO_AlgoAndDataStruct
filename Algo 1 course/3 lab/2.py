f=open('sort.in', 'r')
n=int(f.readline())
a=(f.readline().split())
l=[]

for i in a:
    l.append(int(i))
def heapify(nums, size, index):  
    largest = index
    l_child = (2 * index) + 1
    r_child = (2 * index) + 2

    if l_child < size and nums[l_child] > nums[largest]:
        largest = l_child
    if r_child < size and nums[r_child] > nums[largest]:
        largest = r_child
    if largest != index:
        nums[index], nums[largest] = nums[largest], nums[index]
        heapify(nums, size, largest)
    
def heap_sort(nums):  
    n = len(nums)
    for i in range(n, -1, -1):
        heapify(nums, n, i)
   
    for i in range(n - 1, 0, -1): 
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)

heap_sort(l)
t=open('sort.out','w') 
print(*l , file = t)
t.close()
