"""
Difficulty: Medium

Given a doubly linked list, list nodes also have a child property that can point to a separate doubly linked list. These child lists can also have one or more child doubly linked lists of their own and so on.
Return the list as a single level flattened doubly linked list.

1->2->3->4->5
   |
   6->7->8

Flattened:
1->2->6->7->8->3->4->5

Constraints:
Can a doubly linked list have mulitple child list nodes? -Yes
what do we do with child property after flattening? -Null
"""

from random import randint

class Node:
    def __init__(self, value=None, child=None):
        self.value=value
        self.next=None
        self.prev=None
        self.child=child

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def __iter__(self):
        currNode=self.head
        while currNode:
            yield currNode
            currNode=currNode.next

    def add(self, value, child=None):
        if self.head is None:
            newNode=Node(value)
            self.head=newNode
            self.tail=newNode
            self.child=child
        else:
            self.tail.next=Node(value)
            self.tail.child=child
            self.tail=self.tail.next
        return(self.tail)

    def generate(self,n,min_value,max_value):
        self.head=None
        self.tail=None
        for _ in range(n):
            self.add(randint(min_value,max_value))
        return self
    
    #check
    #assign prev
    def flattenChildren(self):
        currNode=self.head
        while currNode.next is not None:
            while currNode.child is None:
                currNode=currNode.next
            nextNode=currNode.next
            childNode=currNode.child
            currNode.child=None
            currNode.next=childNode
            while childNode.next is not None:
                childNode=childNode.next
            childNode.next=nextNode

LL=LinkedList()
LL.add(1)

LL2=LinkedList()
LL2.add(8)
LL2.add(9)

LL1=LinkedList()
LL1.add(6)
LL1.add(7,LL2)

LL.add(2,LL1)
LL.add(3)
LL.add(4)
LL.add(5)
print ([x.value for x in LL])
LL.flattenChildren()
# LL.generate(10,1,5)
print ([x.value for x in LL])

