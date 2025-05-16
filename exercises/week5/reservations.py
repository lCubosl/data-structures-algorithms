# You are given a list containing reservations as day ranges. Each range is a pair (a,b), where 1 \le a \le b: the reservation 
# starts on the day a and ends on the day b.

# Your task is to determine if the list contains two overlapping reservations, i.e., two ranges with one or more common days.

# For example, the list [(4,7),(1,2)] means that the first reservation is from the day 4 to the day 7, and the second 
# reservation is from the day 1 to the day 2. These two reservations do not ovelap. On the other hand, the reservations on 
# the list [(4,7),(1,5)] do overlap, because both ranges contain the days 4 and 5.

# In a file reservations.py, implement the function check_overlapping that takes a list of reservations as a parameter and 
# returns True if any two ranges overlap, and False otherwise.

# You should implement the function so that it runs efficiently even for long lists. The function should finish immediately 
# in the last two test cases of the code template too.

import random

def check_overlapping(reservations):
  reservations.sort()
  
  if len(reservations) <= 1:
    return False

  for i in range(1, len(reservations)):
    if reservations[i][0] < reservations[i-1][1]:
      return True

  return False

print("expected: False , output:",check_overlapping([])) # False
print("expected: False , output:",check_overlapping([(1, 3)])) # False
print("expected: False , output:",check_overlapping([(4, 7), (1, 2)])) # False
print("expected: True , output:",check_overlapping([(4, 7), (1, 5)])) # True
print("expected: False , output:",check_overlapping([(1, 1), (2, 2)])) # False
print("expected: True , output:",check_overlapping([(1, 1), (1, 1)])) # True
print("expected: True , output:",check_overlapping([(2, 3), (5, 5), (3, 4)])) # True
print("expected: True , output:",check_overlapping([(2, 3), (5, 5), (1, 4)])) # True
print("expected: True , output:",check_overlapping([(2, 3), (5, 5), (1, 5)])) # True

reservations = [(day, day) for day in range(1, 10**5+1)]
random.shuffle(reservations)
print(check_overlapping(reservations)) # False

reservations.append((42, 1337))
random.shuffle(reservations)
print(check_overlapping(reservations)) # True