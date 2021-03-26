from heapq import heappush, heappop
def main():
    fin = open("pathbgep.in")
    fout = open("pathbgep.out", "w")
    n, m = list(map(int, fin.readline().split()))
    matrix = [dict() for i in range(n)]

    for i in range(m):
        a, b, cost = list(map(int, fin.readline().split()))
        a, b = a-1, b-1
        matrix[a][b]= matrix[b][a] = cost

    distance = [None] * n
    q = []
    q.append((0,0))
    
    while q:
        path_len, v = heappop(q)
        if distance[v] is None:
            distance[v] = path_len
            for vertex in matrix[v]:
                edge_len=matrix[v][vertex]
                if distance[vertex] is None:
                    heappush(q, (path_len + edge_len, vertex))

    fout.write(' '.join(str(a) for a in distance))
    fout.close()
    
main()
