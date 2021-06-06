class Priority_queue:
    def __init__(self):
        self.__q = []
        self.__size = 0

    def push_up(self, index):
        k = index
        while k and self.__q[k][1] > self.__q[k // 2][1]:
            self.__q[k // 2], self.__q[k] = self.__q[k], self.__q[k // 2]
            k = k // 2

    def push_down(self, index):
        k = index
        while 2 * k <= self.__size - 1:
            a = k
            if self.__q[2 * k] > self.__q[a]:
                a = 2 * k
            if (2 * k + 1 < self.__size) and (self.__q[2 * k + 1] > self.__q[a]):
                a = 2 * k + 1

            if a != k:
                self.__q[k], self.__q[a] = self.__q[a], self.__q[k]
                k = a
            else:
                break

    def insert(self, value, priority):
        self.__q.append([value, priority])
        self.__size += 1
        self.push_up(self.__size - 1)

    def extract_max(self):
        try:
            self.__q[0], self.__q[self.__size - 1] = self.__q[self.__size - 1], self.__q[0]
            self.__size -= 1
            self.push_down(0)
            return self.__q.pop()
        except IndexError:
            print('Queue is empty! Can not get it')

    def decrease_key(self, value, priority):
        for i in range(self.__size):
            if self.__q[i][0] == value:
                self.__q[i][1] = priority
                self.push_up(i)
                break

    def size(self):
        return self.__size

    def empty(self):
        return self.__size == 0

    ''' additional features '''

    def __str__(self):
        return f"Priority_queue[value, priority]: {[i for i in self.__q]}"


def main():
    q = Priority_queue()
    q.extract_max()


main()
