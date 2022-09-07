
class BT:
    def __init__(self, value=None):
        self.value=value
        self.left=None
        self.right=None
    
def isBalanced(root):
    if root is None:
        return 0
    leftheight = isBalanced(root.left)
    if leftheight==-1:
        return -1
    rightheight= isBalanced(root.right)
    if rightheight==-1:
        return -1
    if abs(leftheight-rightheight)>1:
        return -1
    return max(leftheight,rightheight)+1