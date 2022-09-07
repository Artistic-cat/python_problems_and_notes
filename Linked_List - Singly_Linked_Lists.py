class Node:
    def __init__(self, value=None):
        self.value= value
        self.next= None

class SingleLinkedList:
    def __init__(self):
        self.head= None
        self.tail= None

    #to print the linked list
    def __iter__(self):
        node= self.head
        while node:
            yield node # return from a function without destroying the states of its local variable
            node= node.next
    
    #to traverse manually
    def traverseLL(self):
        if self.head is None:
            print("LL does not exist")
        else:
            node=self.head
            while node is not None:
                print(node.value)
                node=node.next

    #insert to linked list
    def inserttoLL(self, value, location):
        newNode= Node(value)
        if self.head is None:
            self.head=newNode
            self.tail=newNode
        else:
            if location==0:
                newNode.next=self.head
                self.head=newNode
            elif location==1:
                newNode.next=None
                self.tail.next=newNode
                self.tail=newNode
            else:
                tempNode=self.head
                index=0
                while index<location-1:
                    tempNode=tempNode.next
                    index+=1
                nextNode=tempNode.next
                tempNode.next =newNode
                newNode.next=nextNode
                if tempNode==self.tail:
                    self.tail=newNode

singlyLinkedList= SingleLinkedList()

# node1=Node(1)
# node2=Node(2)

# singlyLinkedList.head=node1
# singlyLinkedList.head.next=node2
# singlyLinkedList.tail=node2

singlyLinkedList.inserttoLL(1,0)
singlyLinkedList.inserttoLL(2,0)
singlyLinkedList.inserttoLL(3,1)
singlyLinkedList.inserttoLL(4,3)

print([node.value for node in singlyLinkedList])
