"""
Cycle Detection in a Linked List

Does the linked list only have unique values?
"""

class Node:
    def __init__(self, value=None):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def __iter__(self):
        node=self.head
        while node:
            yield node
            node=node.next

    #Insert to end of linked list
    def insertToList(self,value):
        newNode=Node(value)
        if self.head is None:
            self.head=newNode
        else:
            currNode=self.head
            while currNode.next:
                currNode=currNode.next
            currNode.next=newNode

    def cycleDetection(self):
        currNode=self.head
        seenNode=dict()
        while (currNode not in seenNode):
            if (currNode.next is None):
                return False
            seenNode[currNode]=1
            currNode=currNode.next


LL=LinkedList()
for i in range(1,6):
    LL.insertToList(i)

print([node.value for node in LL])
"""
Optimised with Floyd's Tortoise and Hare Algorithm
Robert Floyd
time O(N)
space O(1)
"""
"""
Hare moves at 2 nodes, tortoise moves at 1 node
Hare checks whether there's a cycle or null
Point where tortoise and hare meet is the meeting point

def HareTortoise(self):
    hare=self.head
    tortoise=self.head
    while True:
        hare=hare.next
        tortoise=tortoise.next
        if hare is Null or hare.next is Null:
            return False
        else:
            hare=hare.next
        if tortoise == hare:
            break
    p1=self.head
    p2=tortoise
    while p1!=p2:
        p1=p1.next
        p2=p2.next
    return p1 #meeting point
"""
