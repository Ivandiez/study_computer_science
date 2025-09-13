class BinaryTree:
    def __init__(self, value):
        self.key = value
        self.left_child = None
        self.right_child = None

    def insert_left(self, value):
        if self.left_child == None:
            self.left_child = BinaryTree(value)
        else:
            bin_tree = BinaryTree(value)
            bin_tree.left_child = self.left_child
            self.left_child = bin_tree

    def insert_right(self, value):
        if self.right_child == None:
            self.right_child = BinaryTree(value)
        else:
            bin_tree = BinaryTree(value)
            bin_tree.right_child = self.right_child
            self.right_child = bin_tree


tree = BinaryTree(1)
tree.insert_left(4)
tree.insert_left(2)
tree.insert_right(6)
tree.insert_right(3)
tree.right_child.insert_left(5)
tree.right_child.left_child.insert_left(7)
tree.right_child.left_child.insert_right(8)


# It'll create a tree:
#      1
#     / \
#    2   3
#   /   / \
#  4   5   6
#     / \
#    7   8


# straight search
def preorder(tree):
    if tree:
        print(tree.key)
        preorder(tree.left_child)
        preorder(tree.right_child)


preorder(tree)
print("-----")  # 1 2 4 3 5 7 8 6


# reverse search
def postorder(tree):
    if tree:
        postorder(tree.left_child)
        postorder(tree.right_child)
        print(tree.key)


postorder(tree)  # 4 2 7 8 5 6 3 1
print("-----")


# symmetric search
def inorder(tree):
    if tree:
        inorder(tree.left_child)
        print(tree.key)
        inorder(tree.right_child)


inorder(tree)  # 4 2 1 7 5 8 3 6
