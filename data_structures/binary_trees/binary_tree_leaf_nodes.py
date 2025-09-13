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

    def has_leaf_nodes(self, root):
        current = [root]
        next = []
        while current:
            leaf = True
            for node in current:
                if node.left_child:
                    next.append(node.left_child)
                    leaf = True
                if node.right_child:
                    next.append(node.right_child)
                    leaf = True
            if leaf:
                return True
            current = next
            next = []
        return False


tree = BinaryTree(1)
tree.insert_left(2)
tree.insert_right(3)
tree.insert_left(4)
tree.left_child.insert_right(6)
tree.insert_right(5)
print(tree.has_leaf_nodes(tree))  # True

# It'll create a tree:
#      1
#     / \
#    4   5
#   / \   \
#  2   6   3
