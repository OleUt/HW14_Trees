class Tree:

    def __init__(self, id_node):
        self.id_node = id_node
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.id_node)

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.id_node)
        if self.right:
            self.right.print_tree()

    # Test 1. Function 'add_nodes' loads list of nodes and inserts them applying function 'insert'
    def add_nodes(self, nodes):
        print('new nodes = ', nodes)
        for i in nodes:
            Tree.__insert(self, i)

    def __insert(self, id_node):
        if self.id_node:
            if id_node < self.id_node:
                if self.left is None:
                    self.left = Tree(id_node)
                else:
                    self.left.__insert(id_node)
            elif id_node > self.id_node:
                if self.right is None:
                    self.right = Tree(id_node)
                else:
                    self.right.__insert(id_node)
        else:
            self.id_node = id_node

    # Test 2. Function finds MIN in BST
    def find_min(self):
        node_min = self.id_node
        if self.left is not None:
            node_min = self.left
            self.left.find_min()
        else:
            print('min = ', node_min)

    # Test 2. Function finds MAX in BST
    def find_max(self):
        node_max = self.id_node
        if self.right is not None:
            node_max = self.right
            self.right.find_max()
        else:
            print('max = ', node_max)


tree = Tree(7)
tree.left = Tree(4)
tree.right = Tree(10)
tree.left.left = Tree(2)
tree.left.right = Tree(6)
tree.right.left = Tree(5)
Tree.print_tree(tree)
print('===================')
tree.add_nodes([8, 1, 15])
Tree.print_tree(tree)
print('===================')
Tree.find_min(tree)
print('===================')
Tree.find_max(tree)
