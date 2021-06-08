def main():
    n, m = map(int, input().split())
    segments = []
    for i in range(n):
        segments.append([*map(int, input().split())])
    points = [int(i) for i in input().split()]
    a = sorted(segments)
    b = sorted(segments, key=lambda mas: mas[1])
    for point in points:
        first = 0
        left = 0
        right = n - 1
        while left < right:

            first = (left + right) // 2
            if a[first][0] <= point:
                left = first + 1
            else:
                right = first - 1
        first = left

        second = 0
        left = 0
        right = n - 1
        while left < right:

            second = (left + right) // 2
            if b[second][1] < point:
                left = second + 1
            else:
                right = second - 1
        second = left

        if a[first][0] <= point:
            first += 1
        if b[second][1] < point:
            second += 1
        print(first - second, end =' ')


main()
