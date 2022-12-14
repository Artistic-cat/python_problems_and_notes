"""
Difficulty: Medium
Reverse specific range in  Linked List

Constraints:
Will m and n always be within bounds of the linked list?
Can we receive m and n for the whole linked list?

1->2->3->4->5
2,4

1->4->3->2->5
"""
from random import randint

class Node:
    def __init__(self, value=None):
        self.value=value
        self.next=None
        self.prev=None

    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def __iter__(self):
        currNode=self.head
        while currNode:
            yield currNode
            currNode=currNode.next
        
    def __str__(self):
        values=[str(x.value) for x in self]
        return('->'.join(values))
    
    def __len__(self):
        result=0
        node=self.head
        while node:
            result+=1
            node=node.next
        return result
    
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

    def reverseSpecificRange(self,start_range,end_range):
        currNode=self.head
        position=1
        while position!=start_range-1:
            currNode=currNode.next
            position+=1
        start=currNode
        currNode=currNode.next
        position+=1
        
        prev=None
        fTail=currNode
        while position!=end_range+1:
            nextVal=currNode.next
            currNode.next=prev
            prev=currNode
            currNode=nextVal
            position+=1
        start.next=prev
        fTail.next=currNode

customLL=LinkedList()
customLL.generate(5,1,30)
print(customLL)
customLL.reverseSpecificRange(2,4)
print(customLL)