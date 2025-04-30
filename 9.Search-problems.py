# 9. Search Problems

# many algorithmic problems can be thought of as search problems, where we have a set of possible 
# solutions and the goal is to find an optimal solution or to count the number of desired solutions

# a straightforward way of solving seach problems is a brute force one that goes through all possible
# solutions one by one. This method always creates the correct answer but the search may take too long 
# to be practical if the number of solutions is big

# if the goal is to find an optimal solutions, there may be a greedy alg that constructs a solution
# efficiently following a certain logic without going through all possibilities. However, a greedy 
# algorithm might not find an optimal solution

# a more advanced method for search problem is dynamic programming, which can be used both for finding
# an optimal solution and for counting solutions.


# Iretating Solutions
# a brute force algorithm for a search problem iterates through all possible solutions one by one. During
# the iteration, the alg can select solutions that satisfy certain conditions or are optimal in some way.

# a brute force algorithm can be implemented to construct all solutions by combining given elements in a
# certain way. 

# Sequences
# the input consists of n elements and we want all sequences of m elements. There are n^m such sequences

# if elements are [1,2,3] and m=2, the sequences are [1,1],[1,2],[1,3],[2,1],[2,2],[2,3],[3,1],[3,2],[3,3]
import itertools

for repetition in itertools.product([1,2,3], repeat=2):
  print(repetition)
print("--------------------------------------------------")
# or (only for repeat 2)
arr = [1,2,3]

for i in arr:
  for j in arr:
    print((i, j))
print("--------------------------------------------------")
# or (general works for any repeat)
def manual_product(arr, repeat, prefix=None):
  if prefix is None:
    prefix = []

  if repeat == 0:
    print(tuple(prefix))
    return

  for item in arr:
    manual_product(arr, repeat-1, prefix+[item])

manual_product([1,2,3], 2)
print("--------------------------------------------------")

# Permutations
# the input ocnsists of n elements and we want all permutations or orderings of the elements.
# the number of permutations is n

# for example, if the elements are [1,2,3] the permutations are [1,2,3],[1,3,2],[2,1,3],[2,3,1],[2,1,3],
# [2,3,1].[3,1,2],[3,2,1]

# In python, permutations of a list can be formed using the function permutations in the module itertools
import itertools

for permutation in itertools.permutations([1,2,3]):
  print(permutation)
print("--------------------------------------------------")
# or (wihtout using extensions)
def permutations(arr):
  if len(arr) == 0:
    return []
  if len(arr) == 1:
    return [arr]
  
  result = []
  for i in range(len(arr)):
    curr = arr[i]
    remaining = arr[:i] + arr[i+1:]
    for p in permutations(remaining):
      result.append([curr] + p)

  return result

for perm in permutations([1,2,3]):
  print(tuple(perm))
print("--------------------------------------------------")

# Example: Orderings
# you are given a positive integer n and your task is to count how many way the elements 1,2,...,n can 
# be ordered so that no pair of adjacent elements are consecutive numbers, i.e, numbers that differ by 1

# ex: n=4, the answer is 2 -> [2,4,1,3],[3,1,4,2] are the only possible ways
import itertools

def count_orders(n):
  items = range(1, n+1)
  count = 0

  for order in itertools.permutations(items):
    if valid_order(order):
      print(order)
      count += 1
  return count

def valid_order(order):
  for i in range(len(order) - 1):
    if abs(order[i] - order[i+1]) == 1:
      return False
  return True

print(count_orders(4))
print("--------------------------------------------------")
# count_orders: iterates through all permutations of the numbers 1...n. For each perm, it calls the 
# fucntion valid_oder that checks if its valid. The solution count is cumputed in the  variable count
# returned at the end.

# count_orders(4) yields the desired answer.

# the algorithm takes O(n!n), because it iterates through all permutations
# the checking of each perm takes O(n)
# since n! grows, the alg is only efficient when n is small

# Example: Balanced parenthesis
# a balanced parenthesis sequence is a string consisting of the chars ( and ) so that it corresponds to 
# a valid mathematical expression. Your  task is to count the number of balanced parenthesis sequences
# of lenght n

# n= 6, answer= 5 because possible banced parentheses are ((())),(())(),()(()),(()()),()()()
import itertools

def count_sequences(n):
  count = 0
  for  sequence in itertools.product("()", repeat=n):
    if valid_sequence(sequence):
      print("".join(sequence))
      count += 1
  return count
  
def valid_sequence(sequence):
  depth = 0
  for bracket in sequence:
    if bracket == "(":
      depth += 1
    if bracket == ")":
      depth -= 1
    if depth < 0:
      return False
  return depth == 0

print(count_sequences(6))
print("--------------------------------------------------")
# count_sequences: iterates through all parenthesis sequences using the function product

# valid_sequence: checks if a sequence is properly balanced. The function goes through the symbols from
# left to right and maintains the parenthesis depth in variable depth.

# time complexity: O(2^n x n) because it goes through 2n parenthesis sequences and the checking of each
# sequences takes O(n)