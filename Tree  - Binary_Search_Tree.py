"""
Binary search trees
"""

class Node:
    def __init__(self, value=None):
        self.value=value
        self.leftChild=None
        self.rightChild=None

def insertNode(root,newNode):
    if root.value==None:
        root.value=newNode
    elif newNode<=root.value:
        if root.leftChild is None:
            root.leftChild=Node(newNode)
        else:
            insertNode(root.leftChild,newNode)
    else:
        if root.rightChild is None:
            root.rightChild=Node(newNode)
        else:
            insertNode(root.rightChild,newNode)

def preOrder(root):
    if root is None:
        return
    print(root.value)
    preOrder(root.leftChild)
    preOrder(root.rightChild)

def levelOrder(root):
    if root is None:
        return
    customQueue=[]
    customQueue.append(root)
    while not customQueue==[]:
        rootNode=customQueue.pop(0)
        print(rootNode.value)
        if rootNode.leftChild is not None:
            customQueue.append(rootNode.leftChild)
        if rootNode.rightChild is not None:
            customQueue.append(rootNode.rightChild)


BST=Node()
insertNode(BST,70)
insertNode(BST,50)
insertNode(BST,90)
insertNode(BST,30)
insertNode(BST,20)
insertNode(BST,40)
insertNode(BST,60)
insertNode(BST,80)
insertNode(BST,100)

levelOrder(BST)