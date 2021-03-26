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
