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
print("--------------------------------------------------")

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

# Removing an element
numbers = [1, 2, 3, 4, 5, 6]
print(numbers)
numbers.pop()
print(numbers)
numbers.pop(1)
print(numbers)
print("--------------------------------------------------")

# original list
# 100 101 102 103 104 105 106 107
# 1   2   3   4   5   6   0   0

# like adding an element, removing it takes O(1) time since other elements are not affected
# 100 101 102 103 104 105 106 107
# 1   2   3   4   5   0   0   0

# removing an element from the midle of the list takes O(n) time since other elements are affected 
# and need to be shifted to other memory locations
# 100 101 102 103 104 105 106 107
# 1   3   4   5   0   0   0   0

# remove() removes first occurence of the element
numbers = [1, 2, 3, 1, 2, 3]
numbers.remove(3)
print(numbers)
print("--------------------------------------------------")
# time complexity O(n) since other elements in memory are affected

# Summary
# Indexing ([])               O(1)
# size (len)                  O(1)
# Is element on list (in)     O(n)
# searching (index)           O(n)
# counting (count)            O(n)
# add to end (append)         O(1)
# add to middle (insert)      O(n)
# remove from end (pop)       O(1)
# remove from middle (pop)    O(n)
# search and remove (remove)  O(n)

# references and copying
# In python, lists and other data structures are acessed thorugh references. Assigning to variable
# only copies the reference, not the contents of the list
a = [1, 2, 3, 4]
b = a
a.append(5)
print(a)
print(b)
print("--------------------------------------------------")
# a and b refeer to the same list in memory. if an element is changed in a, it also changes in b

# to copy contents, we can copy()
a = [1, 2, 3, 4]
b = a.copy()
a.append(5)
print(a)
print(b)
print("--------------------------------------------------")
# copying referece (a = b) takes O(1)
# copying list using copy() takes O(n)

# side effects of functions
def double(numbers):
  result = numbers
  for i in range(len(result)):
    result[i] *= 2
  return result

numbers = [1, 2 ,3, 4]
print(numbers)
print(double(numbers))
print(numbers)
print("--------------------------------------------------")
# since only the reference is copied, the function changes the list it got as a parameter

def double(numbers):
  result = numbers.copy()
  for i in range(len(result)):
    result[i] *= 2
  return result

# copy() fixes the problem
numbers = [1, 2 ,3, 4]
print(numbers)
print(double(numbers))
print(numbers)
print("--------------------------------------------------")

# Slicing and concatenation
# slice operator ([:]) creates a new list that contains a copy of a segment of the given list
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print(numbers[2:6])
print(numbers)
print("--------------------------------------------------")
# this operator needs O(n) time because it copies contents from old list to new list
result = numbers.copy
result = numbers[:]
# the preview lines are equivalent

# + can be use to concatenate lists
first = [1, 2, 3, 4]
second = [5, 6, 7, 8]
print(first + second)
print("--------------------------------------------------")
# takes O(n) because operator copies the elements from the original lists to new list