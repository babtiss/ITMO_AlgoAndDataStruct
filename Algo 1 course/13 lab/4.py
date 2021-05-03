def prefix(s):
    len_s = len(s)
    pref = [0]*len_s
    for i in range(1,len_s):
        k = pref[i-1]
        while k > 0 and s[i] != s[k]:
            k = pref[k-1]
        if s[i] == s[k]:
            k += 1
        pref[i] = k
    return pref

def make_kmp(s,alphabet):
    
    d='abcdefghijklmnopqrstuvwxyz'
    s+='#'
    n=len(s)
    pi = prefix(s)
    aut=[[0 for j in range(alphabet) ]for i in range(n)]

    for i in range(n):
        for j in range(alphabet):
            c=d[j]
            if i and c!=s[i]:
                aut[i][j]=aut[pi[i-1]][j]
            else:
                key=0
                if c==s[i]:
                    key=1
                aut[i][j]=i+key
                
    for i in aut:
        print(*i)
        
def main():     
    n=int(input())
    s=input().split()
    s=s[0]
    make_kmp(s,n)
main()
