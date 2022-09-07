"""
Remove Duplicates

1->2->2->3->3->4
1->2->3->4
"""
from random import randint

class Node:
    def __init__(self, value=None):
        self.value=value
        self.next=None
        self.prev=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def __iter__(self):
        currNode=self.head
        while currNode:
            yield currNode
            currNode=currNode.next

    def add(self, value):
        if self.head is None:
            newNode=Node(value)
            self.head=newNode
            self.tail=newNode
        else:
            self.tail.next=Node(value)
            self.tail=self.tail.next
        return(self.tail)

    def generate(self,n,min_value,max_value):
        self.head=None
        self.tail=None
        for _ in range(n):
            self.add(randint(min_value,max_value))
        return self
    #with temp variable
    def checkDups(self):
        if self.head is None:
            return
        currNode=self.head
        visited=set([currNode.value])
        while currNode.next:
            if currNode.next.value in visited:
                currNode.next=currNode.next.next
            else:
                visited.add(currNode.next.value)
                currNode=currNode.next

LL=LinkedList()
LL.generate(10,1,5)
print ([x.value for x in LL])
LL.checkDups()
print ([x.value for x in LL])