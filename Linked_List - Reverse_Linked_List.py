"""
Reverse Linked Lists

Question:
Given a linked list, return it's reverse

Verify it's constraints:
What do we return if we get null or a single node?

Test case:
12345 # 54321
1 # 1
Null # Null
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

    #Check this
    def reverseLL(self):
        prev=None
        current=self.head
        while current:
            next=current.next
            current.next=prev
            prev=current
            current=next

LL=LinkedList()
for i in range(1,6):
    LL.insertToList(i)

print([node.value for node in LL])

LL.reverseLL()

print([node.value for node in LL])