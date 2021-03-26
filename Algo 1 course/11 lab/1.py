
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
