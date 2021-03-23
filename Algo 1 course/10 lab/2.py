'''
1.  Алгоритм Прима
2.  List - плохо по памяти, хорошо по скорости
    Array - хорошо по памяти, плохо по скорости
    Нужно правильно подобрать соотношение скорости/памяти, чтоб прошло по тестам 
'''
def main():
    def length(x1,x2,y1,y2):
        return (x2-x1)*(x2-x1) + (y2-y1)*(y2-y1)
     
    f=open("spantree.in")
    t=open("spantree.out", "w")
    n=int(f.readline())
    inf=1000000000
    coor=[None for i in range(n)]
    l=[[0]*n for i in range(n)]
     
    for i in range(n):
        a,b=list(map(int, f.readline().split()))
        a,b=a-1,b-1
        coor[i]=[a,b]
         
    for i in range(n):
        x1=coor[i][0]
        y1=coor[i][1]
        for j in range(i):
            x2=coor[j][0]
            y2=coor[j][1]
            l[i][j]=l[j][i]=length(x1,x2,y1,y2)
           
    dist=[inf]*n
    viz=[0]*n
    dist[0]=0
    for i in range(n):
        cur=None
       
        for j in range(n):
            if not viz[j] and (cur is None or dist[j]<dist[cur]):
                cur=j
                 
        viz[cur]=1
        for j in range(n):
            if not viz[j] and l[cur][j]<dist[j]:
                dist[j]=l[cur][j]
       
    print(sum(a**0.5 for a in dist),file=t)
    t.close()
main()
