class TreeNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def is_leaf(self):
        return not (self.right or self.left)

    def has_any_children(self):
        return self.right or self.left

    def has_both_children(self):
        return self.right and self.left

    def pre_order(self, node):

        if node:
            print(node.value, end=' ')
            self.pre_order(node.left)
            self.pre_order(node.right)

    def post_order(self, node):
        if node:
            self.post_order(node.left)
            self.post_order(node.right)
            print(node.value, end=' ')

    def in_order(self, node):
        if node:
            self.in_order(node.left)
            print(node.value, end=' ')
            self.in_order(node.right)

    def find_value(self, item):
        if item < self.value:
            if self.left is None:
                return False
            return self.left.findval(item)
        elif item > self.value:
            if self.right is None:
                return False
            return self.right.findval(item)
        else:
            return True

    def minimum(self):
        while self.left is not None:
            self.left.minimum()
        return self.value

    def maximum(self):
        while self.right is not None:
            self.right.maximum()
        return self.value

    def insert(self, value):

        if self.value:
            if value < self.value:
                if self.left is None:
                    self.left = TreeNode(value)
                else:
                    self.left.insert(value)
            elif value > self.value:
                if self.right is None:
                    self.right = TreeNode(value)
                else:
                    self.right.insert(value)
        else:
            self.value = value


class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def put(self, item):
        self.size += 1
        if self.root is None:
            self.root = TreeNode(item)
        else:
            self.root.insert(item)

    def write(self):
        if self.root:
            print('\npre_order')
            self.root.pre_order(self.root)
            print('\nin_order')
            self.root.in_order(self.root)
            print('\npost_order')
            self.root.post_order(self.root)
            print()


def main():
    q = BinarySearchTree()
    q.put(2)
    q.put(3)
    q.write()


main()
