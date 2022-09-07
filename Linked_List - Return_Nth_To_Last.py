"""
Return Nth to last
"""

from random import randint

class Node:
    def __init__(self, value=None):
        self.value=value
        self.next=None
    
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def __iter__(self):
        currNode=self.head
        if currNode:
            yield currNode
            currNode=currNode.next
    
    def add(self, value):
        newNode=Node(value)
        if self.head is None:
            self.head=newNode
            self.tail=newNode
        else:
            self.tail.next=newNode
            self.tail=self.tail.next
        return(self.tail)
    
    def generate(self, n, start, end):
        self.head=None
        self.tail=None
        for _ in range(n):
            self.add(randint(start,end))
        return self

    def valueFromLast(self,steps):
        currNode=self.head
        pointNode=self.head
        while steps!=0 and pointNode.next:
            pointNode=pointNode.next
        while pointNode.next:
            currNode=currNode.next
            pointNode=pointNode.next
        return(currNode.value)

LL=LinkedList()
LL.generate(10,1,5)
print([x.value for x in LL])

print(LL.valueFromLast(4))
