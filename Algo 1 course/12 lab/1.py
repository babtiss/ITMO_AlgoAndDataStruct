def main():
    n = int(input())
    l = [int(j) for j in input().split()]
    path = [-1]*n
    cur = [1]*n
    mx = -1
    last_cur = -1
    for i in range(n):
        for j in range(i):
            if (l[i]>l[j]) and (cur[j]+1>cur[i]) :
                cur[i]=cur[j]+1
                path[i]=j
    for i in range(n):
        if cur[i]>mx:
            mx=cur[i]
            last_cur = i
    answer = []
    while True:
        answer.append(l[last_cur])
        last_cur = path[last_cur]
        if last_cur == -1:
            break
    print(mx)
    print(*answer[::-1])
main()
