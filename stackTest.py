from stackLib import *

stackTest = stack() #create an instance of a class object
print("Newly instantiated stack:")
print(stackTest.dispStack()) #show what the stack looks like
print("")

stackTest.push(0) #add int "0" to the stack
print("Add 0 to the stack:")
print(stackTest.dispStack()) #show what the stack looks like using dispStack() <---Method 1
print("")

print("Add 1 to the stack:")
print(stackTest.push(1)) #add int "1" to the stack, show what the stack looks like directly from push() <---Method 2
print("")

print("Add Hello to the stack:")
print(stackTest.push("Hello")) ##add str "Hello" to the stack, show what the stack looks like
print("")

print("Length of stack now:")
print(stackTest.lenStack()) #show the length of the stack
print("")

print("Let's pop off 2 items, 1 at a time:")
print(stackTest.pop()) #show what the stack looks like after popping off last-added item
print(stackTest.pop()) #pop off another element
print("")

print("Is the stack empty?:")
print(stackTest.isEmpty()) #check if stack is empty
print("")

print("Then, let's pop off the last element:")
print(stackTest.pop()) #show what the stack looks like after popping off last item
print("")

print("Now, the stack should be empty. Correct?:")
print(stackTest.isEmpty()) #check if stack is empty