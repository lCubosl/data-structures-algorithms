# You are given a list that consists of the numbers 1 ... n. A pair of indices (i,j) is an inversion if i<j and the element at index i on the 
# list is greater than the element at index j.

# You may assume that n is at most 100.
# In a file inversions.py, implement a function count that returns the total number of inversions in the list.

def count(t):
  # base case, length of array is 0 or 1
  if len(t) <= 1:
    return 0
  
  # O(n**2) not optimal for big algorithms
  inversion = 0
  n = len(t)
  for i in range(n):
    for j in range(i + 1, n):
      if t[i] > t[j]:
        inversion += 1
  
  return inversion

print(count([1,3,2])) # 1
print(count([1])) # 0
print(count([4,3,2,1])) # 6
print(count([1,8,2,7,3,6,4,5])) # 12
# Explanation: The list [4,3,2,1] contains the inversions (0,1), (0,2), (0,3), (1,2), (1,3) and (2,3).