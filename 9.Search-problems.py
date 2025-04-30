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

# Speeding up the search
# the 2 preceding examples implement the search by generating all solutions and checking each solution.
# it works but does a lot of  unnecessary work in processing invalid solutions

# let us consider balanced parenthesis sequence. Many of the sequences are invalid at the beggining
# since they start with ")", eliminating half of the sequences.
# when n=20, the alg goes through 2^20 = 1048576 sequences, but about only 16796 or 1/60 are valid

# another factor slowing down algs: even though we only need to count the solutions, the alg actually 
# constructs all solutions. 

# more efficient al for counting parenthesis
def count_sequences(n, d=0):
  if d < 0 or d > n:
    return 0
  if n == 0:
    return 1
  return count_sequences(n-1, d+1) + count_sequences(n-1, d-1)

print(count_sequences(6))
print("--------------------------------------------------")
# this function doesnt use the module itertools to construc solutions, but iterates through the solutions 
# directly using recursion. 
# the parameter (n) tells how many additional symbols are still needed and the parmeter (d) mantains the
# parenthesis depth of the current sequence (0) at the begining, when the sequence is empty
# in each step, there are 2 possibilities ")" and "("
# ")": decreases the depth
# "(": increases the depth

# each step checks if the current sequence can still lead to valid solution. if it becomes negative (d<0),
# or de depth is greater than the number of remaining symbols, (d>n), the sequence automaticaly returns 0
# if all symbols have been added and n==0, it returns 1

# Greedy algorithms
# efficient method for finding an optimal solution without going through all possible solutions. greedy
# algs are often simple but their correctness can be difficult to justify

# You have access to an unbouded number of coins with values 1,2 and 5. what is the minimum number of 
# coins needed to form the sum x
# x=13, answer=13 (1,2,5,5)

def find_coins(x):
  solutions = [[]]

  for solution in solutions:
    if sum(solution) == x:
      print(solution)
      return len(solution)
    for coin in [1,2,5]:
      solutions.append(solution + [coin])

print(find_coins(13))
print("--------------------------------------------------")
# the function returns the first combination summing up to x, returning the size

# the function 1st goes through all combinations of 1 coin, 2 coins, 3 coins and finally, at 4 coins, it
# discovers [1,2,5,5] that sum up to 13.

# correct algorithm but needs a  lot of time when the number needed is large

# using greedy algs, that go through the coin values from largest to smallest can be a better and faster
# solution.
def find_coins(x):
  count = 0
  for coin in [5,2,1]:
    while coin <=x:
      x -= coin
      count += 1
  return count

print(find_coins(13))
print("--------------------------------------------------")
# this alg is efficient because it does not iterate through all solutions but constructs an optimal 
# solution.

# Why the algorithm is correct
# when designing a greedy alg, it cna be difficult to justify that the alg computes an optimal
# solution in all cases. Greedy algs don't go through all solutions and there is risk that the 
# constructed solution is not optimal 

# how do we know that the greedy alg constructs a solution with the smallest number of coins?

# our greedy alg is correct but if we change our coin values to [1,4,5], it becomes incorrect. It produces
# [1,1,1,5,5] instead of [4,4,5]

# lets prove that the greedy alg finds an optimal solution when the coin values are 1,2,5. assume that 
# there is a situation, where the current sum is still at least 5 short of the largest sum, but it is 
# incorrect to add more coins of value 5. the remaining sum must be achieved by using the coins of value 
# 1 and 2 at least 3 more coins is needed. but no set of 3 coins 1 or 2 is optimal
  # 1,1,1 -> 1,2
  # 1,1,2 -> 2,2
  # 1,2,2 -> 5
  # 2,2,2 -> 1,5

# Algorithm checking

coins = [1,4,5]
def find_coins_brute(x):
  solutions = [[]]

  for solution in solutions:
    if sum(solution) == x:
      return len(solution)
    for coin in coins:
      solutions.append(solution + [coin])

def find_coins_greedy(x):
  count = 0
  for coin in reversed(coins):
    while coin <= x:
      x -= coin
      count += 1
  return count

x = 1
while True:
  result_brute = find_coins_brute(x)
  result_greedy = find_coins_greedy(x)

  if result_brute != result_greedy:
    print("different answer for", x, "coins")
    print("brute:", result_brute)
    print("greedy:", result_greedy)
    break

  x += 1

# x=8 is the smallest case, where the greedy alg produces an incorrect answer, for the coin vals [1,4,5]