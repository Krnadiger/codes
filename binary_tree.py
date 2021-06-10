class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    
class Tree:
    def __init__(self,data=None):
        self.root = Node(data)

    def _insert(self, node, data):
        if node == None:
            return Node(data)
        if data < node.data:
            node.left  = self._insert(node.left, data)
        else:
            node.right = self._insert(node.right, data)
        return node

    def insert(self,data):
        if self.root.data == None:
            self.root.data = data
            return
        node = self.root
        self._insert(node,data)

    def tree_right_view(self):
        current_node = self.root
        while(current_node.right != None):
            print(current_node.data)
            current_node = current_node.right
        print(current_node.data)

    def tree_left_view(self):
        current_node = self.root
        while(current_node.left != None):
            print(current_node.data)
            current_node = current_node.left
        print(current_node.data)

    def _inorder(self,root):
        if root != None:
            self._inorder(root.left)
            print(root.data, end = ' ')
            self._inorder(root.right)

    def inorder(self):
        current_root = self.root
        self._inorder(current_root)


    def _height(self,node):
        if node == None:
            return 0
        else:
            lheight = self._height(node.left)
            rheight = self._height(node.right)
            if lheight > rheight :
                return lheight+1
            else:
                return rheight+1

    def height(self):
        node = self.root
        return self._height(node)



tree = Tree()
print(tree.root == None)

tree.insert(5)
print(tree.root.data)

