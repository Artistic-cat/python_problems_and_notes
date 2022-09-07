"""
Check if a tree is a BST
"""

class BT:
    def __init__(self,value=None):
        self.value=value
        self.leftChild=None
        self.rightChild=None

def validateBST(root,mini,maxi):
    if root.value>=mini and root.value<=maxi:
        if root.leftchild:
            validateBST(root.leftChild,mini,root.value)
        if root.rightChild:
            validateBST(root.rightChild,root.value,maxi)
    else:
        return False
    return True