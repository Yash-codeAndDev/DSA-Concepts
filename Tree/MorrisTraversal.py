from BST_template import BinaryTree

class MorrisTraversal:
    def inorder(self, root):
        current = root
        while current:
            if current.left is None:
                print(current.val)
                current = current.right
            else:
                predecessor = current.left
                while predecessor.right and predecessor.right != current:
                    predecessor = predecessor.right
                
                if predecessor.right is None:
                    predecessor.right = current
                    current = current.left
                else:
                    predecessor.right = None
                    print(current.val)
                    current = current.right

    def preorder(self, root):
        current = root
        while current:
            if current.left is None:
                print(current.val)
                current = current.right
            else:
                predecessor = current.left
                while predecessor.right and predecessor.right != current:
                    predecessor = predecessor.right
                
                if predecessor.right is None:
                    predecessor.right = current
                    print(current.val)
                    current = current.left
                else:
                    predecessor.right = None
                    current = current.right


if __name__ == '__main__':
    tree = BinaryTree()
    tree.insert(80)
    tree.insert(40)
    tree.insert(120)
    tree.insert(10)
    tree.insert(60)
    tree.insert(5)
    tree.insert(30)
    tree.insert(100)
    tree.insert(190)
    tree.insert(110)

    morris = MorrisTraversal()

    morris.inorder(tree.root)