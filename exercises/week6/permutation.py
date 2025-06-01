# A list is a permutation if it contains the numbers 1,2,\dots,n exactly once each. For example, the 
# lists [1], [2,1] and [3,1,2,4] are permutations.

# In a file permutation.py, implement the class PermutationTracker with the following methods:
  # append(number): add number to the end of the list
  # check(): return True, if the list is a permutation, and False otherwise

# The time complexity of both methods should be O(1).
class PermutationTracker:
  def __init__(self):
    pass

  def append(self, number):
    pass

  def check(self):
    pass

tracker = PermutationTracker()

tracker.append(1)
print(tracker.check()) # True

tracker.append(4)
print(tracker.check()) # False

tracker.append(2)
print(tracker.check()) # False

tracker.append(3)
print(tracker.check()) # True

tracker.append(2)
print(tracker.check()) # False

tracker.append(5)
print(tracker.check()) # False

# Here the contents of the list change as follows:

# [1] (is a permutation)
# [1,4] (is not a permutation)
# [1,4,2] (is not a permutation)
# [1,4,2,3] (is a permutation)
# [1,4,2,3,2] (is not a permutation)
# [1,4,2,3,2,5] (is not a permutation)

# You can test the efficiency of your solution using the following code. In this case too the code 
# should finish almost immediately.
tracker = PermutationTracker()
total = 0
for i in range(10**5):
  if i%2 == 0:
    tracker.append(i + 2)
  else:
    tracker.append(i)
  if tracker.check():
    total += 1
print(total) # 50000