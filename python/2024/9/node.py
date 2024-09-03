# 1. class node
# 2. class tree
# 3. set root
# 4. get node
# 5. create node
# 6. in order, pre order, post order

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def set_root(self, node):
        self.root = node

    def get_node(self):
        return self.root

    def create_node(self, data, left=None, right=None)
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
        self.pre_order(node.right)

    def post_order(self, node)
        if node is None:
            return

        self.post_order(node.left)
        self.post_order(node.right)
        print(node.data)

