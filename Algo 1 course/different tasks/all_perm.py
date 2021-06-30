def permutations(a: list, n: int):
    j = n - 2
    k = n - 1
    while j != -1 and a[j] > a[j + 1]:
        j -= 1
    if j == -1:
        return False
    while k and a[j] >= a[k]:
        k -= 1
    a[j], a[k] = a[k], a[j]
    l = j + 1
    r = n - 1
    while l < r:
        a[l], a[r] = a[r], a[l]
        l += 1
        r -= 1
    return True


def main():
    n = int(input())
    a = [i for i in range(1, n + 1)]
    print(*a)
    while permutations(a, n):
        print(*a)


main()
