class Node:
    def __init__(self, data=0):
        self._data = data
        self._next = None

    def get_data(self):
        return self._data

    def get_next(self):
        return self._next

    def set_data(self, data):
        self._data = data

    def set_next(self, next):
        self._next = next


class Unordered_list:
    def __init__(self):
        self._head = None
        self._count = 0

    def is_empty(self):
        return self._head is None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self._head)
        self._head = temp
        self._count += 1

    def search(self, item):
        found = False
        current = self._head
        while current:
            if current.get_data() == item:
                found = True
                break
            current = current.get_next()
        return found

    def remove(self, item):
        current = self._head
        previous = None
        found = False
        while not found and current:
            if current.get_data() == item:
                found = True
                break
            previous = current
            current = current.get_next()
        if found:
            if previous is None:
                self._head = current.get_next()
            else:
                previous.set_next(current.get_next())
        else:
            print('Такого элемента в списке нет')

    def get_way(self):
        current = self._head
        while current:
            print(current.get_data(), end='->')
            current = current.get_next()
        print('|')

    def size(self):
        return self._count


def main():
    mylist = Unordered_list()
    mylist.add(31)
    mylist.add(54)
    mylist.add(17)
    mylist.get_way()
    mylist.remove(17)
    mylist.get_way()


if __name__ == '__main__':
    main()
