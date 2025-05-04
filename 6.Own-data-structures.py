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
print("--------------------------------------------------")
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
print("--------------------------------------------------")

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
print("method len", len(s))
print("--------------------------------------------------")

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
class SuperStack:
  def __init__(self):
    self.stack = []

  def push(self, x):
    self.stack.append((1, x))
  
  # this method has a loop, taking O(n) time. We want O(1)
  def push_many(self, k, x):
    self.stack.append((k, x))

  def top(self):
    return self.stack[-1][1]
  
  def pop(self):
    last = self.stack[-1]
    if last[0] == 1:
      self.stack.pop()
    else:
      self.stack[-1] = (last[0] - 1, last[1])
  
  def __repr__(self):
    return str(self.stack)

s = SuperStack()
s.push_many(3, 8)
s.push(4)
s.push(4)
s.push_many(2, 5)
print(s)
print("--------------------------------------------------")

# Example: Mode
# Implement a class Mode with the following methods
  # add(x): add number x on the list
  # mode(): return the mode of the list, the most frequent number on the list
# time complexity O(1)

class Mode:
  def __init__(self):
    self.count = {}
    self.status = (0, 0)

  def add(self, x):
    if x not in self.count:
      self.count[x] = 0
    self.count[x] += 1
    self.status = max(self.status, (self.count[x], x))
  
  def mode(self):
    return self.status[1]
  
m = Mode()
m.add(1)
m.add(1)
m.add(2)
print(m.mode()) # 1
m.add(2)
m.add(2)
print(m.mode()) # 2
print("--------------------------------------------------")