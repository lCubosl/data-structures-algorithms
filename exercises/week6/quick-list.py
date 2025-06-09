# Implement a class QuickList with the following methods:
  # move(k): move the first k elements of the list to the end of the list
  # get(i): return the element at the index i

# The initial contents of the list is given as a parameter to the constructor. The time complexity of both methods should be O(1).
# In a file quicklist.py, implement a class QuickList according to the following template:
class QuickList:
  def __init__(self, t):
    pass

  def move(self, k):
    pass

  def get(self, i):
    pass

q = QuickList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(q.get(4)) # 5
q.move(3)
print(q.get(4)) # 8
q.move(3)
print(q.get(4)) # 1
q.move(10)
print(q.get(4)) # 1
q.move(7)
q.move(5)
print(q.get(0)) # 9

# Explanation: The contents of the list in the example changes as follows:
  # [1,2,3,4,5,6,7,8,9,10]
  # move(3) -> [4,5,6,7,8,9,10,1,2,3]
  # move(3) -> [7,8,9,10,1,2,3,4,5,6]
  # move(10) -> [7,8,9,10,1,2,3,4,5,6]
  # move(7) -> [4,5,6,7,8,9,10,1,2,3]
  # move(5) -> [9,10,1,2,3,4,5,6,7,8]