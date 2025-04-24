# 4. Hashing
# Hashing is a technique that is frequently used in implementing efficient algorithms.
# In python, set() and dict() are based on hashing

# set
# mantains a set of elements. The operations on the data structure include
  # add - adds element to set
  # in - finds given element in set
  # remove - removes element from set
# data structure is implemented so that all of the above take O(1) time
numbers = set()
numbers.add(1)
numbers.add(2)
numbers.add(3)
print(numbers)
print("--------------------------------------------------")

# we can also create a set directly form a list
numbers = set([1,2,3])
print(numbers)
print("--------------------------------------------------")

# in tests if element is in set
print("3 in numbers:", 3 in numbers)
print("4 in numbers:", 4 in numbers)
print("--------------------------------------------------")

# we can add and remove element from the set using remove
print(numbers)
numbers.remove(2)
print(numbers)
print("--------------------------------------------------")

# list and set are similar data structures. Both mantain a collection of elements and support additions
# and removals. However, tere are other differences in their efficiency and other properties

# OPERATION              | LIST | SET
# operation (append/add) | O(1) | O(1)
# finding (in)           | O(n) | O(1)
# removing (remove)      | O(n) | O(1)

# indexing
# a list supports indexing (elements can be acessed)
numbers = [1,2,3]
print(numbers[1])
print("--------------------------------------------------")

# a set does  not
numbers = set([1,2,3])
#print(numbers[1]) # typeErrorL object is not subscriptable
print("--------------------------------------------------")

# Repeated elements
# in a list, an element can occur multiple times
numbers = []
numbers.append(5)
numbers.append(5)
numbers.append(5)
print(numbers)
print("--------------------------------------------------")

# a set contains an element at most once
numbers = set()
numbers.add(5)
numbers.add(5)
numbers.add(5)
print(numbers)
print("--------------------------------------------------")

# Example: How many numbers
# you are given a list of numbers. how many distinct numbers does it contain?
# [3,1,2,1,5,2,2,3] a:4
def count_dist(nums):
  seen = []
  for n in nums:
    if n not in seen:
      seen.append(n)
  return(len(seen))
print("expected: 4, output:", count_dist([3,1,2,1,5,2,2,3]))
print("--------------------------------------------------")
# takes O(n^2) because for every number in nums, it has to check if that number is already on the list
# O(n) x O(n) = O(n^2)

def count_dist(nums):
  seen = set()
  for n in nums:
    seen.add(n)
  return(len(seen))
print("expected: 4, output:", count_dist([3,1,2,1,5,2,2,3]))
print("--------------------------------------------------")
# takes O(n) since the list is only looped once and adds every number to the set.
# due to the nature of the set, repeated numbers are not added

# can be simplified to:
def count_dist(nums):
  return(len(set(nums)))
print("expected: 4, output:", count_dist([3,1,2,1,5,2,2,3]))
print("--------------------------------------------------")

# Dictionary
# dict or dictionary is based on hashing and stores key-value pairs. 
# The idea is that we can use the key to retrieve the associated value.
# dictionary can be seen as a generalization of a list
# keys are arbitrary objects
# adding and removing data using keys takes O(1)

weights = {}
weights["apina"] = 100
weights["banaani"] = 1
weights["cembalo"] = 500
# or
weights = {"apina": 100, "banaani": 1, "cembalo": 500}

print(weights["apina"])
weights["apina"] = 150
print(weights["apina"])
print("--------------------------------------------------")

# in checks if a given key is in the dictionary
print("apina" in weights)
print("ananas" in weights)
print("--------------------------------------------------")

# del removes a key and the associated value from a dictionary
print(weights)
del weights["banaani"]
print(weights)
print("--------------------------------------------------")

# Using a dictionary
# Has an element occured
# can be used similarly to a set to keep track of elements that have been seen
def elements(items):
  seen = {}
  for x in items:
    seen[x] = True
# this code has aproximately the same functionality as the followin code
def elements(items):
  seen = set()
  for x in items:
    seen.add(x)

# counting occurences
# counting element occurences is a common use for dictionaries
def count_occurence(items):
  count = {}
  for x in items:
    if x not in count:
      count[x] = 0
    count[x] += 1
  return count
print(count_occurence([1,2,3,4,4,3,4,1,2]))
print("--------------------------------------------------")

# position of occurence
# track where each element has occured
def position_occurence(items):
  pos = {}
  for i, x in enumerate(items):
    pos[x] = i
  return pos
print(position_occurence([1,2,3,4,4,3,4,1,2]))
print("--------------------------------------------------")

# example Mode
# You are given a list of numbers, and your task is to compute the mode, which is the most frequent
# number on the list. If the mosde is not unique, you can choose any of the possible choices 
# for the most freqauent number
# list = [1,2,3,2,2,3,2,2], a = 2
def find_mode(numbers):
  count = {}
  mode = numbers[0]

  for n in numbers:
    if n not in count:
      count[n] = 0
    count[n] += 1

    if count[n] > count[mode]:
      mode = n
  return mode

print("mode:", find_mode([1,2,3,2,2,3,2,2]))
print("mode:", find_mode([1,2,3,4,4,3,4,1,2]))
print("--------------------------------------------------")
# since dictionary operations take O(1) time, complexity of algorithm is O(n)
# for loop takes O(n). Nested in it, we are looking into the count dictionary O(1)
# O(n) x O(1) = O(n x 1) = O(n)

# here is another way to implement the same code
def find_mode(numbers):
  count = {}
  mode = (0, 0)

  for n in numbers:
    if n not in count:
      count[n] = 0
    count[n] += 1

    mode =  max(mode, (count[n], n))
  return mode[1]

print("mode:", find_mode([1,2,3,2,2,3,2,2]))
print("mode:", find_mode([1,2,3,4,4,3,4,1,2]))
print("--------------------------------------------------")

# Example: Rounds
# You are given a list that contains the numbers 1,2,..., n in some order. Your task is to collect all 
# the numbers in order form smallest to largest so taht in each round you go through the list from left 
# to right. How many rounds do you need?
# list = [3,6,1,7,5,2,4,8], rounds=4

# solution list (dictionary)
def count_rounds(numbers):
  n = len(numbers)
  rounds = 1
  for i in range(1, n):
    if numbers.index(i+1) < numbers.index(i):
      rounds += 1
  return rounds

print("list = [3,6,1,7,5,2,4,8], expected: 4, output:", count_rounds([3,6,1,7,5,2,4,8]))
print("--------------------------------------------------")
# algorithm is slow. Going through the list takes O(n) and the index takes an aditional O(n)
# O(n) x O(n) = O(n^2)

# Efficient solution
def count_rounds(numbers):
  n = len(numbers)
  pos = {}
  for i, x in enumerate(numbers):
    pos[x] = i
  
  rounds = 1
  for i in range(1, n):
    if pos[i + 1] < pos[i]:
      rounds += 1
  return rounds

print("list = [3,6,1,7,5,2,4,8], expected: 4, output:", count_rounds([3,6,1,7,5,2,4,8]))
print("--------------------------------------------------")
# now, locating numbers only takes O(1). Each of the loops takes O(n) but they are separate loops
# O(n) time

# Example: Playlist
# You are given a play list, where each song is represented by an integer. Your task is to find 
# out how long is the longest part of the play list that contains no song twice
# example: playlist = [1,2,1,3,5,3,2,1], answer = 5

# song   | 1 2 1 3 5 4 3 1
# length | 1 2 2 3 4 5 3 4

def max_length(songs):
  pos = {}
  start = 0
  length = 0

  for i, song in enumerate(songs):
    if song in pos:
      start = max(start, pos[song] + 1)
    length = max(length, i - start + 1)
    pos[song] = i
  
  return length

print("expected: 4, outuput:", max_length([1,2,1,3,5,3,2,1]))
print("--------------------------------------------------")
# O(n) time complexity since pos is a dictionary that takes O(1) and the loop takes O(n) time