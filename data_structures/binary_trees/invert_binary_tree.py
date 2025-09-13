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

    def invert_using_breadth_first(self):
        current = [self]
        next = []
        while current:
            for node in current:
                if node.left_child:
                    next.append(node.left_child)
                if node.right_child:
                    next.append(node.right_child)
                tmp = node.left_child
                node.left_child = node.right_child
                node.right_child = tmp
            current = next
            next = []


def invert_using_depth_first(root):
    if root:
        root.left_child, root.right_child = invert_using_depth_first(root.right_child), invert_using_depth_first(
            root.left_child
        )
        return root


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


def print_tree(tree, level=0):
    if tree:
        print_tree(tree.right_child, level + 1)
        print(" " * 4 * level + "-> " + str(tree.key))
        print_tree(tree.left_child, level + 1)


print_tree(tree)

tree.invert_using_breadth_first()

print("Inverted:")
print_tree(tree)
print("-----")

invert_using_depth_first(tree)
print_tree(tree)
