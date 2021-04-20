def main():
    fin=open("knapsack.in")
    fout=open("knapsack.out", "w")
    sd=fin.readline().split()
    
    s,n=int(sd[0]),int(sd[1])
    sd=fin.readline().split()
    l=[int(j) for j in sd]
    bag=[0]*(s+1)
    bag[0]=1
    t=0
    for i in l:
        for j in range(t,-1,-1):
            k=i+j
            if bag[j] and k<=s:
                bag[k]=1
                if k>t:
                    t=k
    print(t,file=fout)
main()
