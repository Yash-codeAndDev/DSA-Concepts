class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if key < node.val:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert_recursive(node.left, key)
        elif key >= node.val:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert_recursive(node.right, key)

    def display_inorder(self):
        self._display_inorder_recursive(self.root)

    def _display_inorder_recursive(self, node):
        if node is not None:
            self._display_inorder_recursive(node.left)
            print(node.val)
            self._display_inorder_recursive(node.right)
    
if __name__ == "__main__":
    BST_Tree = BinaryTree()
    num_nodes = int(input("Enter the number of nodes in the tree: "))
    print("Enter the nodes:")
    for _ in range(num_nodes):
        key = int(input())
        BST_Tree.insert(key)

    print("Inorder Traversal of BST:")
    BST_Tree.display_inorder()
