'''
ФОРД-БЕЛМАН значит. Тут будет много букав.

Поясняю за код:
distance[] расстояние от вершины s до i-ой. 
edges[] список всех рёбер
path[] откуда мы пришли в i-ую вершину.

Алгоритм:
1) Идея
Для нахождения кратчайших путей от одной вершины до всех остальных, воспользуемся методом динамического программирования.
Алгоритм Беллмана-Форда позволяет очень просто определить, существует ли в графе G отрицательный цикл, достижимый из вершины s. 
Достаточно произвести внешнюю итерацию цикла не |V|-1, a ровно |V| раз. 
Если при исполнении последней итерации длина кратчайшего пути до какой-либо вершины строго уменьшилась, то в графе есть отрицательный цикл, 
достижимый из s. На основе этого можно предложить следующую оптимизацию: отслеживать изменения в графе и, как только они закончатся,
сделать выход из цикла (дальнейшие итерации будут бессмысленны).
2) Реализация
i-ый шаг. Мы достраиваем пути длины i-1 до путей длины i, пытаясь найти маршрут меньшего веса (как и в обычном Ф-Б)
flag - проверка, если нашёлся более короткий путь, flag будет поднят --> алгоритм продолжается, иначе нет смысла больше итерировать.
Очевидно, что если есть цикл отрицательного веса, то flag будет поднят даже после последней итерации. 
Теперь нам нужно просто вывести цикл отрицательного веса. 
Сначала поднимемся с помощью path[] до корня цикла ( если так не сделать - не факт что в данный момент мы вообще в вершине цикла)
Теперь добавим все вершины цикла в список ( надеюсь читатель разберёт код сам).
Кто спросит - сложность O(n*m)
'''
def main():
    fin=open("negcycle.in")
    fout=open("negcycle.out", "w")
  
    inf = 10**9
    n=int(fin.readline())
    distance=[0]*n
    edges=[]
    path=[None]*n
    
    for i in range(n):
        sd=fin.readline().split()
        for j in range(n):
            if int(sd[j])!=inf:
                edges.append([i,j,int(sd[j])])
                
    len_edges=len(edges)
    flag=None
    for i in range(n):
        flag=None
        for j in range(len_edges):
            e0,e1,e2=edges[j]
            if distance[e1]>distance[e0]+e2:
                distance[e1]=max(-inf,distance[e0]+e2)
                path[e1]=e0
                flag=e1
        if flag is None:
            break
                    
    if flag is not None:
        for i in range(n):
            flag=path[flag]
        answer_path=[]
        cur=flag
        while True:
            answer_path.append(cur+1)
            cur=path[cur]
            if cur==flag:
                answer_path.append(cur+1)
                break
        
        print('YES',file=fout)
        print(len(answer_path),file=fout)
        print(*answer_path[::-1],file=fout)
    else:
        print('NO',file=fout)
    fout.close()
                                 
main()
