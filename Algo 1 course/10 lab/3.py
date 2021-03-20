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
