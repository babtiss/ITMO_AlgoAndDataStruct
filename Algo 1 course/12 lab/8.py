#Число всех подпалиндромов в строке
def rec(l,r):
    global d,a
    if d[l][r]==-1:
        if s[l]==s[r]:
            d[l][r]=rec(l+1,r)+rec(l,r-1)+1
        else:
            d[l][r]=rec(l+1,r)+rec(l,r-1)-rec(l+1,r-1)
    return d[l][r]%a
 
n=int(input())
s=[int(j) for j in input().split()]
a=10**9

d=[[int(1) if i==j else int(0) if i<j else int(-1) for i in range(n)] for j in range(n)]
print(rec(0,n-1)%a)
