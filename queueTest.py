from queueLib import *

queueTest = queue() #create an instance of a class object
print("Newly instantiated queue:")
print(queueTest.dispQueue()) #show what the queue looks like
print("")

queueTest.enqueue(0) #add int "0" to the queue
print("Add 0 to the queue:")
print(queueTest.dispQueue()) #show what the queue looks like using dispQueue() <---Method 1
print("")

print("Add 1 to the queue:")
print(queueTest.enqueue(1)) #add int "1" to the enqueue, show what the enqueue looks like directly from enqueue() <---Method 2
print("")

print("Add Hello to the queue:")
print(queueTest.enqueue("Hello")) ##add str "Hello" to the queue, show what the queue looks like
print("")

print("Length of queue now:")
print(queueTest.lenQueue()) #show the length of the queue
print("")

print("Let's take off 2 items, 1 at a time:")
print(queueTest.dequeue()) #show what the queue looks like after taking away the first-added element
print(queueTest.dequeue()) #dequeue another element
print("")

print("Is the queue empty?:")
print(queueTest.isEmpty()) #check if queue is empty
print("")

print("Then, let's dequeue the remaining element:")
print(queueTest.dequeue()) #show what the queue looks like after dequeuing remaining item
print("")

print("Now, the queue should be empty. Correct?:")
print(queueTest.isEmpty()) #check if queue is empty
