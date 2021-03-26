def main():
    fin=open("pathsg.in")
    fout=open("pathsg.out", "w")
    sd = fin.readline().split()
    inf = 9444433322110099900
    n,m= int(sd[0]), int(sd[1])
    matrix=[[inf]*n for i in range(n)]
    for i in range(m):
        sd = fin.readline().split()
        a,b,cost=int(sd[0]),int(sd[1]),int(sd[2])
        a-=1
        b-=1
        matrix[a][b]=cost
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i==j:
                    matrix[i][j]=0
                else:
                    matrix[i][j]=min(matrix[i][j], matrix[i][k]+matrix[k][j])
    for i in matrix:
        for j in i:
            print(j,end=' ', file = fout)
        print(file=fout)
    fout.close()
                                 
main()
