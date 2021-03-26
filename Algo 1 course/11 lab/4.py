def main():
    def dfs(v):
    
        visited[v]=1
        for vert in graph[v]:
            if not visited[vert]:
                dfs(vert)
       
    fin = open("path.in")
    fout = open("path.out", "w")
   
    inf = 10**20
    n, m, s = list(map(int, fin.readline().split()))
    distance = [inf]*n
    distance[s-1] = 0
    edges = []
    path = [None] * n
    graph = [[] for i in range(n)]
   
    for i in range(m):
        a, b, cost = list(map(int, fin.readline().split()))
        a-=1
        b-=1
        edges.append([a, b, cost])
        graph[a].append(b)
    neg_cycle=[]
    for i in range(n+1):
        flag=None
        neg_cycle=[]
        for j in range(m):
            e0,e1,e2=edges[j]
            if distance[e0] != inf:
                if distance[e1] > distance[e0]+e2:
                    distance[e1] = distance[e0]+e2
                    path[e1] = e0
                    flag = e1
                    neg_cycle.append(e1)
        if flag is None:
            break
    visited=[0]*n
    if flag:
        for i in neg_cycle:
            if visited[i]==0:
                dfs(i)
       
  
    for i in range(n):
        if visited[i]:
            distance[i] = '-'
    
    for elem in distance:
        if elem==inf:
            print('*',file=fout)
        else:
            print(elem,file=fout)
            
   
    fout.close()
   
main()
