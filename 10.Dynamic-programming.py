# 10. Dynamic Programming

# dynamic programming is an algorithmic technique that can be used for efficiently solving many search 
# problems.

# You have an unlimited number of coins with values given as a list. Each value is positive integer and 
# the smallest value is 1. The goal is to choose a set of coins summing up to x
  # 1. Find the optimal solution: how many coins at least is needed to achieve sum x
  # 2. Construct an optimal solution: Give an example of a minimal set of coins summing up to  x
  # 3. Count solutions: hwo many different ways there are to achieve sum x
# [1,2,5] x=13, answers are
  # 1. smalles number of coins: 4
  # 2. minimal soluution: [1,2,5,5]
  # 3. count solutions: 634

# Finding the optimal solution
# the basic idea of dynamic programming is to solve a problem with the help of smaller cases of the 
# same problem, called subproblems.
# sum x: subproblems are the cases where the  target sum is 0...x - 1
  # coin value 1. other coins must sum up to x=12
  # coin value 2. other coins must sum up to x=11
  # coin value 5. other coins must sum up to x=8

# we know the smalles t n of coins to achieve sum x=8,11,12, we can find the smallest number of coins
# summing up to x=13 by taking the minimum of the three cases and adding 1
  # to solve x=13, we first need to solve
    # x=8
    # x=11
    # x=12
    # these subproblems can be solved similarly by dividing them into smaller subproblems

# we can turn this idea into a pratical dynamic programming alg by solving all subproblems x=0,... x
# from smallest to largest

def min_coins(x, coins):
  result = {}

  result[0] = 0
  for s in range(1, x + 1):
    result[s] = s
    for c in coins:
      if s - c >= 0:
        result[s] = min(result[s], result[s-c] + 1)

  return result[x] 

print(min_coins(13, [1, 2, 5])) # 4
print(min_coins(13, [1, 4, 5])) # 3
print(min_coins(42, [1, 5, 6, 17])) # 5
print("--------------------------------------------------")
# the function defines a disctionary "result" that stores the smallest number of coins needed 
# for each sum 0...x the first step records sum 0 needs 0 coins. then the alg goes through all the 
# otehr sums in the loop.

# since one of the coin values is 1, all the sums 0...x can be formed using cois. the initial value is
# set to s which corresponds to choosing only coins of value 1

# unlike the greedy algorithm, the dynamic programing produces the right output.
# time complexity: O(n x m). 
  # n is the number of coin values and 
  # m is the target sum.
# this enables efficient computation even in fairly big cases that would be far too big for a brute force

# Constructing an optimal solution
# now we will modify the previous code so that it produces the set of coins
# x=13, coins=[1,2,5], solution=[1,2,5,5]

def min_coins(x, coins):
  result = {}

  result[0] = []
  for s in range(1, x + 1):
    result[s] = [1] * s
    for c in coins:
      if c in coins:
        if s-c >= 0:
          new_result = result[s-c] + [c]
          if len(new_result) < len(result[s]):
            result[s] = new_result

  return sorted(result[x])

print(min_coins(13, [1, 2, 5]))
print(min_coins(13, [1, 4, 5]))
print(min_coins(42, [1, 5, 6, 17]))
print("--------------------------------------------------")
# inside the loop, the alg constructs a list new_result from the list corresponding to the sum s-c.
# appending a coin value c to the subproblme  list proguces the shortest list that sums up to s and has 
# c as the last coin.

# Counting Solutions
# dynamic programming can also be used for counting the number of all solutions. ex: when the coin values
# are [1,2,5] tgere are 634 different ways to chioose a list of coins with the sum x=13
def count_coins(x, coins):
  result = {}

  result[0]=1
  for s in range(1, x+1):
    result[s]=0
    for coin in coins:
      if s-coin >=0:
        result[s] += result[s-coin]

  return result[x]

print(count_coins(13, [1, 2, 5]))
print(count_coins(13, [1, 4, 5]))
print(count_coins(42, [1, 5, 6, 17]))
print("--------------------------------------------------")

# Example: Subsequences
# you are given a list of n integers. your task is to find how long is the longest increasing subsequence
# i.e, how many numbers can we collect from the list going from left to right so that each number is larger
# than the previous number. It is allowed to skup numbers
# ex: [4,1,5,6,3,4,3,8], longest subsequence is [1,3,4,8], len=4
def find_longest(items):
  res = {}

  max_len=0
  for i in range(len(items)):
    res[i] = 1
    for j in range(i):
      if items[j] < items[i]:
        res[i] = max(res[i], res[j]+1)
    max_len= max(max_len, res[i])
  
  return max_len

print(find_longest([4, 1, 5, 6, 3, 4, 1, 8]))
print("--------------------------------------------------")
# time complexity O(n^2) since it has 2 nested loops
# The number of all possibilities is O(2^n), so this is faster than a brute force

# Example: Balanced Parenthesis (v2 with dynamic programing)
# a balanced parenthesis sequence is a string consisting of the chars ( and ) so that it corresponds to 
# a valid mathematical expression. Your  task is to count the number of balanced parenthesis sequences
# of lenght n

# n= 6, answer= 5 because possible banced parentheses are ((())),(())(),()(()),(()()),()()()

def count_sequences(n, d=0, result={}):
  if d < 0 or d > n:
    return 0
  if n == 1:
    return 1
  if (n,d) not in result:
    result[(n, d)] = count_sequences(n-1, d+1) + count_sequences(n-1, d-1)
  
  return result[(n,d)]

print(count_sequences(100))
print("--------------------------------------------------")
# dynamic programming subproblmes are pairs of the form(n, d), where n is the number of parenthessis
# symbols that still needs to be added, d is the parenthesis depth of the current sequence. dictionary
# "result" contains the answers for all parameter combinations that have already been computed by earlier
# calls of the func.
# the answer is computed by recursion only if it has not been computed previously. otherwise its in the
# dictionary

# since each call is time complex O(1) and the number of parameter combinations is O(n^2), the time
# complexity its also O(n^2)

# this next solution is another dynamic programming way of solving the problem w only 1 parameter
def count_sequences(n, res={}):
  if n==0:
    return 1
  if n not in res:
    count = 0
    for i in range(2, n+1, 2):
      count += count_sequences(i-2) * count_sequences(n-i)
    res[n] = count
  return res[n]

print(count_sequences(100))
print("--------------------------------------------------")
# each function call takes O(n), number of parameter combinations O(n), O(n) x O(n) = O(n^2)
# its also time complex O(n^2)

# Nested Recursion
# implementic a dynamic program algorithm with recursion can lead to deeply nested recursive 
# calls, which can cause problmes when executing the code. The following does not work as desired
print(count_sequences(2000))
print("--------------------------------------------------")
# the execution of the code causes an error "RecursionError: max recursion depth exceedded in comparison"

# in python, the limit ofr nested recursive calls is fairly small.
# the limit can be raised using "setrecursionlimit" in the module sys

import sys
sys.setrecursionlimit(5000)
print("sys recursion limit 5000 \n", count_sequences(2000))
print("--------------------------------------------------")
# now the code should work and give the desired result

# changing the recursion limit can be problematic because it can cause issues with python exe environment.
# an alternative aproach is to modigy the dynamic programming implementation so that it uses loops instead
# of recursion
def count_sequences(n, d=0, result={}):
  if d < 0 or d > n:
    return 0
  if n == 1:
    return 1
  if (n,d) not in result:
    result[(n, d)] = count_sequences(n-1, d+1) + count_sequences(n-1, d-1)
  
  return result[(n,d)]
# we can remove the recursion by finding a suitable order for computing the subproblmes so that when 
# a subproblme result is neede, it has already been computed and stored in the dic result
# implementation is as follows:
def count_sequences(n):
  res = {}
  res[(0,0)] = 1

  for i in range(1, n+1):
    res[(0, i)] = 0

  for i in range(1, n+1):
    for j in range(0, n+1):
      res[(i,j)] = 0
      if j+1 <= n:
        res[(i,j)] += res[(i-1,j+1)]
      if j-1 >=0:
        res[(i,j)] += res[(i-1,j-1)]
  
  return res[(n,0)]

print(count_sequences(2000))
print("--------------------------------------------------")
# this implementation does not use recursion and has no problmes with the recursion limit.