# Implement a class Mex with the following method:

# add(x): add the number x to the list and return the mex number of the list

# The mex number of a list is the smallest non-negative integer that does not occur on the list. For example, the mex number of the 
# list [2,0,3,4,2] is 1.

# The method add should take O(1) time on average. You may assume that all the numbers added to the list are non-negative.

# In a file mex.py, implement a class Mex according to the following template:
class Mex:
  def __init__(self):
    self.numbers = []
    self.seen = set()
    self.mex = 0

  def add(self, x):
    self.seen.add(x)
    #
    return self.mex

m = Mex()
print(m.add(1)) # 0
print(m.add(3)) # 0
print(m.add(4)) # 0
print(m.add(0)) # 2
print(m.add(5)) # 2
print(m.add(2)) # 6