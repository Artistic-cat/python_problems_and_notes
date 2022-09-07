"""

Question:
Implement the class Queue using stacks. The queue methods you need to implement are enqueue, dequeue, peek and empty

enqueue- append value to end of queue
dequeue- remove the value from the start of the queue
peek- see the start of the queue
empty- boolean to see if queue is empty

Constraints?
same space and time complexity the same as normal queues?

"""

class Queue:
    def __init__(self):
        self.inqueue=[]
        self.outqueue=[]
    
    def enqueue(self,val):
        self.inqueue.append(val)

    def dequeue(self,val):
        if len(self.outqueue)==0:
            while(len(self.inqueue)):
                self.outqueue.append(self.inqueue.pop())
        return self.outqueue.pop()
    
    def peek(self):
        if (len(self.outqueue)==0):
            while(len(self.inqueue)):
                self.outqueue.append(self.inqueue.pop())
        return self.outqueue[len(self.outqueue)-1]
    
    def empty(self):
        return (len(self.inqueue)==0 and len(self.outqueue)==0)
