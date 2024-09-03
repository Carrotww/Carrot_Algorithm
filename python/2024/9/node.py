class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

# tree class
# set node
# get node
# inorder, preorder, postorder

class Tree:
    def __init__(self):
        self.root = None

    def set_root(self, node):
        self.root = node

    def get_node(self):
        return self.root

    def create_node(self, data, left=None, right=None):
        node = Node(data)
        node.left = left
        node.right = right
        return node

    def in_order(self, node)
        if node is None:
            return
        self.in_order(node.left)
        print(node.data)
        self.in_order(node.right)

    def pre_order(self, node)
        if node is None:
            return
        print(node.data)
        self.pre_order(node.left)
        self.pre_order(node.right)%

    def post_order(self, node)
        if node is None:
            return
        self.post_order(node.left)
        self.post_order(node.right)
        print(node.data)

