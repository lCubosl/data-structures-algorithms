# Implement a class TrackRepeat with the following methods:
  # add(x, k): add the number x to the list k times
  # check(): return True if each number on the list has a different number of occurrences, and otherwise False

# The time complexity of both methods should be O(1).
# For example, the list [1,3,1,1,2,3,1] contains three distinct numbers 1, 2 and 3. The number 1 occurs 4 times, the number 2 occurs 1 times, 
# and the number 3 occurs 2 times. Thus each number has a different number of occurrences (4, 1 and 2 occurrences).

# In a file trackrepeat.py, implement a class TrackRepeat according to the following template:
class TrackRepeat:
  def __init__(self):
    self.numbers = []

  def add(self, x, k):
    pass

  def check(self):
    pass

t = TrackRepeat()
print(t.check()) # True
t.add(1, 3)
print(t.check()) # True
t.add(2, 3)
print(t.check()) # False
t.add(2, 2)
print(t.check()) # True
t.add(3, 1)
print(t.check()) # True
t.add(3, 4)
print(t.check()) # False