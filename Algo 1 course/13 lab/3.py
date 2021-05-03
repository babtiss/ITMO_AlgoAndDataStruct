# Время
# Префикс-функция от строки S строится за O(S)=O(P+T). 
# Проход цикла по строке S содержит O(T) итераций. Итого, время работы алгоритма оценивается как O(P+T).
# Память
# Предложенная реализация имеет оценку по памяти O(P+T). 
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
 
def main():
    fin = open("prefix.in")
    fout = open("prefix.out", "w")
    parse = fin.readline().split()
    s = parse[0]
    answer = prefix(s)
    print(*answer,file = fout)
main()
