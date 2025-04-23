# List in memory
a = 7
b = -3
c = [1, 2, 3, 1, 2]
d = 99

# contents stored in memory starting from adress 100
# 100 101 102 103 104 105 106 107 108 109 110
# 7   -3  1   2   3   1   2   0   0   0   99
# a   b   c                               d
# list "c" only has 5 elements but has 3 aditional memory slots reserved to prepare for possible addition 
# of new elements
# c[2] = addres 102 + 2 = 104

# list operations
# most have the following complexities
# O(1): Opp always efficient
# O(n): Opps efficiency depends on the size of the array
  
# indexing
# items can be accessed and modified using idx opperator []
# O(1)
numbers = [4, 3, 7, 3, 2]
print(numbers[2])
numbers[2] = 5
print(numbers[2])
print("--------------------------------------------------")

# List size
# O(1) because length is stored in memory with list
numbers = [4, 3, 7, 3, 2]
print(len(numbers))
print("--------------------------------------------------")

# searching
# O(n) worst case, it has to search through the entire list to find indexed number
numbers = [4, 3, 7, 3, 2]
print(3 in numbers) #True
print(8 in numbers) #False
print(numbers.index(3)) #1
print(numbers.count(3)) #2
print("--------------------------------------------------")

def count(items, target):
  result = 0
  for item in items:
    if item == target:
      result += 1
  return result
# if element is in the beggining of the list, operator is fast. 
# Worst case scenario, it has to go through the entire list once -> O(n)

# Adding an element
# .append() method adds element at the end of list
# .insert() method adds element to given position in the list

numbers = [1, 2, 3, 4]
print(numbers)
numbers.append(5)
print(numbers)
numbers.insert(1, 6)
print(numbers)

# original list
# 100 101 102 103 104 105 106 107
# 1   2   3   4   0   0   0   0

# append() needs O(1) time because adding elements to the end of the list doesnt require cahnges to 
# other memory locations
# 100 101 102 103 104 105 106 107
# 1   2   3   4   5   0   0   0

# insert() requires time complexity O(n) because when element is added, other elements need to be moved 
# forward to make room for the new element
# 100 101 102 103 104 105 106 107
# 1   6   2   3   4   5   0   0 