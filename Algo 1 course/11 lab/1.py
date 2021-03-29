'''
Класический Дейкстра, для хранения величин расстояний используем массив. Получаем O(n^2).
distance[] - расстояние от вершины s, до i-ой
visited[] - флаг, покажем True, если мы точно нашли min расстояние до i-ой вершины.

Шаг алгоритма:
1) Если все вершины посещены, алгоритм завершается (логично).
2) В противном случае, из ещё не посещённых вершин выбирается вершина index_min_weight, к которой ведёт минимальный путь min_weight.
3) Для каждого z соседа вершины index_min_weight, кроме отмеченных как посещённые (visited[]), рассмотрим новую длину пути,
 равную сумме значений пути до вершины index_min_weight и веса ребра index_min_weight-->j.
 Запишем такое значение в переменную a (просто захотел) , теперь сравним distance[z] и a. 
4) Рассмотрев всех соседей, пометим вершину u как посещённую и повторим шаг алгоритма.

'''
def main():
    fin = open("pathmgep.in")
    fout = open("pathmgep.out", "w")
    inf = 9444433322110099900
    sd=fin.readline().split()
    n,s,f = int(sd[0]), int(sd[1]), int(sd[2])
    s,f = s-1, f-1
    distance = [inf]*n
    visited = [False]*n
    distance[s] = 0
    matrix = []

    for i in range(n):
        matrix.append(list(map(int, fin.readline().replace('-1', str(inf)).split())))

    for i in range(n):
        min_weight = inf
        index_min_weight = None
        for j in range(n):
            if not(visited[j]) and distance[j] < min_weight:
                min_weight = distance[j]
                index_min_weight = j
        if min_weight == inf:
            break
        for z in range(n):
            a=distance[index_min_weight] + matrix[index_min_weight][z]
            if a < distance[z]:
                distance[z] = a
        visited[index_min_weight] = True

    if distance[f] == inf:
        print(-1, file = fout)
    else:
        print(distance[f], file = fout)
    fout.close()

main()
