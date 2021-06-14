def rec(k):
    global l, prev, inf
    if l[k]:
        return l[k]
    a, b = inf, inf
    c1, c2 = 0, 0
    if k % 3 == 0:
        c1 = k // 3
        a = rec(c1)
    else:
        c1 = k - 1
        a = rec(c1)
    if k % 2 == 0:
        c2 = k // 2
        b = rec(k // 2)
    if a < b:
        l[k] = a + 1
        prev[k] = c1
    else:
        l[k] = b + 1
        prev[k] = c2
    return l[k]


n = int(input())
inf = 1000000000
l = [0] * (n + 1)
l[1] = 1
prev = [-1] * (n + 1)
rec(n)
print(l[n] - 1)
answer = []
p = n
while p > 0:
    answer.append(p)
    p = prev[p]

print(*answer[::-1])
