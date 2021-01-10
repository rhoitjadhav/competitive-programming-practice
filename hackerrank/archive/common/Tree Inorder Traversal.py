Tree : Top View
def inOrder(root):
    if root is None:
        return

    inOrder(root.left)
    print(root.info, end=" ")
    inOrder(root.right)


tree = BinarySearchTree()
arr = list(map(int, "1 2 5 3 4 6".split()))

for i in range(len(arr)):
    tree.create(arr[i])

inOrder(tree.root)
