# 6. Own data structures
# The functionality of a data structure can be represented as a collection of methods, each with given 
# parameters and a given result from calling it.
# ex: list has the methods append, count, index.

# By defining a class we can create a customized data structure that has its own set of methods.
# The advantage of a class is that it offers a clean inteface that hides the details of the 
# internal implementation

# Example: Stack
# Implement a class Stack that implements the stack data structure. The class should have the following 
# methods
  # push(x): adds element to top of the stack
  # top(): access the element at the top of the stack
  # pop(): remove element at the top of the stack

class Stack:
  def __init__(self):
    self.stack = []
  def push(self, x):
    self.stack.append(x)
  def top(self):
    return self.stack[-1]
  def pop(self):
    self.stack.pop()

s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.top()) # 3
print(s.top()) # 3
s.pop()
print(s.top()) # 2
print("--------------------------------------------------")
# if we know how the class is implemented, we can access the internal data too
s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.stack)
print("--------------------------------------------------")

# How not to implement a class
# the following does not work
class Stack:
  stack = []

  def push(self, x):
    self.stack.append(x)
  def top(self):
    return self.stack[-1]
  def pop(self):
    self.stack.pop()
# The difference to the previous class is that there is no constructor method (__init__) and the list
# stack is created at the main level of the class.

a = Stack()
b = Stack()

a.push(1)
b.push(2)
print(a.top())
# the stack is shares by all objects created form the class.
# since the stack is shared, push puts both 1 and 2 into the same stack even though they are 2 different
# variables

# Aditional class features
# __repr__ produces a description of the contents of the stack as a string. 
class Stack:
  def __init__(self):
    self.stack = []
  def push(self, x):
    self.stack.append(x)
  def top(self):
    return self.stack[-1]
  def pop(self):
    self.stack.pop()
  def __repr__(self):
    return str(self.stack)

# after this change, we can print out the contents of the stack
s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s)

# another feature missing. We cannot determine the size of the stack with the function len(). We can fix
# this by adding a mehtod __len__
class Stack:
  def __init__(self):
    self.stack = []
  def push(self, x):
    self.stack.append(x)
  def top(self):
    return self.stack[-1]
  def pop(self):
    self.stack.pop()
  def __repr__(self):
    return str(self.stack)
  def __len__(self):
    return len(self.stack)

# method __len__ is called when an object of the class is given as parameter to the function len.
s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(len(s))

# additionaly, pop and top don't have error handling for cases where the list is empty
class Stack:
  def __init__(self):
    self.stack = []

  def push(self, x):
    self.stack.append(x)

  def top(self):
    if len(self.stack) == 0:
      raise IndexError("top from empty stack")
    return self.stack[-1]
  
  def pop(self):
    if len(self.stack) == 0:
      raise IndexError("pop from empty stack")
    self.stack.pop()

  def __repr__(self):
    return str(self.stack)
  
  def __len__(self):
    return len(self.stack)

# s = Stack()
# s.push(1)
# s.pop()
# s.pop() # IndexError: pop from empty stack

# Example: Eddicient duplicates
# Implement a class SuperStack with the following methods:
  # push(x): add element x to the top of the stack
  # push_many(k, x): add k copies of the element x to the top of the stack
  # top(): access the element at the top of the stack
  # pop(): remove the element at the top of the stack
# time complexity of each method should be O(1)