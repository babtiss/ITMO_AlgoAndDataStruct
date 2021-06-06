class Node:
    def __init__(self, value, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value


class ZNode:
    def __init__(self, value, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value


def convert(root):
    if root:
        a = root.value
        l = root.left
        r = root.right
        return ZNode(a, convert(l), convert(r))
    else:
        return None


def main():
    a = Node(1)
    b = convert(a)
    print(b.__class__)


main()
