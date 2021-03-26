'''
Краскал.
Реализация с использованием структуры данных "система непересекающихся множеств" (DSU),
которая позволит достигнуть асимптотики O (E × log (V)).

1. Откуда асимптотика:
Отсортируем все рёбра по неубыванию веса. 
Затем поместим каждую вершину в своё дерево (т.е. своё множество) с помощью вызова функции DSU union за O(N). 
Перебираем все рёбра и для каждого ребра за O(1) определяем, принадлежат ли его концы разным деревьям (с помощью двух вызовов find за O (1)).
Наконец, объединение двух деревьев будет осуществляться вызовом Union - также за O (1). Итого мы получаем асимптотику O (E log V + V + E) = O (E log V).

2. Как работает DSU:
Мы заводим массив parent, в котором для каждого элемента мы храним ссылку на его предка в дерева.
find - определяет какому дереву/множеству принадлежит данная вершина (для этого нужен parent ).
jopa - проверка случая, когда обе вершины принадлежат одному дереву.
union - объединяет 2 указанных множества (множества для первой и второй вершины)
rank - определяет размер дерева ( число вершин в множестве), чтобы ускорить алгоритм
будем присоединять дерево с меньшим рангом к дереву с большим рангом. 

'''

def main():
    def find(v):
        nonlocal parent
   
        while (v != parent[v]):
            v=parent[v]
        return v
     
    def jopa(v1,v2):
        return find(v1)==find(v2)
     
    def union():
        nonlocal parent, rank, a, b, c, answer
   
        v1=find(a)
      
        v2=find(b)
        if rank[v1]>rank[v2]:
            v1,v2=v2,v1
        rank[v2]+=rank[v1]
        parent[v1]=v2
       
 
    n,m=map(int,input().split())
    edges=[]
    parent = [i for i in range(n)]
    rank=[1]*n
     
    for i in range(m):
        a, b, c = map(int,input().split())
        edges.append([c, a - 1, b - 1])
    edges.sort()
     
    answer=0
    for i in range(m):
        c,a,b=edges[i]
        if not jopa(a,b):
            union()
            answer+=c
 
    print(answer)
      
   
main()
