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

def kmp(p,t):
    p_len = len(p)
    t_len = len(t)
    pref = prefix(p+'#'+t)
    
    min_len = min(p_len,t_len)
    answer = []
    for i in range(len(pref)):
        if pref[i] == min_len:
            answer.append(i-2*p_len+1)
    return answer  
 
def main():
    fin = open("search1.in")
    fout = open("search1.out", "w")
    parse = fin.readline().split()
    p = parse[0]
    parse = fin.readline().split()
    t = parse[0]
    
    answer = kmp(p,t)
    print(len(answer),file = fout)
    print(*answer,file = fout)
main()
