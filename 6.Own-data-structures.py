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
