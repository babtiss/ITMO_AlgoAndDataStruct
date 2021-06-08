count = 0


def merde_sort(mas):
    global count
    length = len(mas)
    if length == 1:
        return mas

    a = length // 2
    left = merde_sort(mas[:a])
    right = merde_sort(mas[a:])
    left_id = 0
    right_id = 0
    answer = []
    len_left = len(left)
    len_right = len(right)
    while True:
        if left_id == len_left and right_id == len_right:
            break
        elif left_id == len_left:
            answer.append(right[right_id])
            right_id += 1
        elif right_id == len_right:
            answer.append(left[left_id])
            left_id += 1
        else:
            if left[left_id] <= right[right_id]:
                answer.append(left[left_id])
                left_id += 1
            else:
                answer.append(right[right_id])
                count += len_left - left_id
                right_id += 1
    return answer


def main():
    global count
    n = int(input())
    l = [int(j) for j in input().split()]
    merde_sort(l)
    print(count)


main()
