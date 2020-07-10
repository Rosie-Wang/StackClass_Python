#Class for queue: first in first out (FIFO structure)
class queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item): #adds to top of queue
        temp = self.items[:]  # create a temporary local copy of original queue
        self.items = temp + [item]
        return self.items

    def dequeue(self): #removes from bottom of queue
        size = len(self.items)
        temp = self.items[:]  # create a temporary local copy
        self.items = temp[1:size]
        return self.items

    def dispQueue(self): #allows us to see all elements in the queue
        return self.items

    def lenQueue(self): #determine the length of the queue
        return len(self.items)

    def isEmpty(self): #check if queue is empty
        if self.items == []:
            return True
        else:
            return False
