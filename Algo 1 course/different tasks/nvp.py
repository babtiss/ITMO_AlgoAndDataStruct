n = int(input())
*l, = map(int, input().split())
inf = 10 ** 10
d = [-inf] * (n + 1)
d[0] = inf
pos = [-1] * (n + 1)
prev = [-1] * (n + 1)
mx = 0
for i in range(n):
    left = 0
    right = n
    while left + 1 < right:
        middle = (left + right) // 2
        if d[middle] < l[i]:
            right = middle
        else:
            left = middle

    if d[right - 1] >= l[i] > d[right]:
        d[right] = l[i]
        pos[right] = i
        prev[i] = pos[right - 1]
        mx = max(mx, right)

p = pos[mx]
answer = []
while p != -1:
    answer.append(p+1)
    p = prev[p]


print(len(answer))
print(*answer[::-1])
