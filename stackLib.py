#Class for stack: last in first out (LIFO structure)

class stack:
    def __init__(self):
        self.items = [] #empty list

    def push(self,item): #adds item to top of stack
        temp = self.items[:] #create a temporary local copy
        self.items = temp + [item]
        return self.items

    def pop(self): #deletes item at the top of stack
        size = len(self.items)
        temp = self.items[:]  # create a temporary local copy
        self.items = temp[0:size-1]
        return self.items

    def dispStack(self): #allows us to see all elements in the stack
        return self.items

    def lenStack(self): #determine the length of the stack
        return len(self.items)

    def isEmpty(self): #check if stack is empty
        if self.items == []:
            return True
        else:
            return False

