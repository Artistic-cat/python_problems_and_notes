
def inOrder(root,n):
    if not root:
        return
    inOrder(root.leftChild)
    print(root.value)
    inOrder(root.rightChild)