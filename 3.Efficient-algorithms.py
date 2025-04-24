# 3. Efficient algorithms

# A straight forward algorithm is usually O(n^2). This can usually be called a brute force algorithm
# If n is big, a more efficient algorithm might be needed

# An efficient algorithm is often required to have a time complexity of O(n) or O(n logn)
# Typically has a single loop that goes through the input from left to right.
# The code inside is efficient so that each round in the loop takes O(1). Then the whole algo takes O(n)

# ex: stock trading
# day   | 0 1 2 3 4 5 6 7
# price | 3 7 5 1 4 6 2 3
# buy day 3, sell day 5
import random

def best_profit_brute(prices):
  n = len(prices)
  best = 0
  for i in range(n):
    for j in range(i + 1, n):
      best = max(best, prices[j] - prices[i])
  return best

print("best profit:", best_profit_brute([3,7,5,1,4,6,2,3]))
print("--------------------------------------------------")
# O(n^2) because "best" is being computer for each combination of days
# For bigger lists it is not efficient

# consider a single loop algorithm that might work
# when the loop reaches a given day, what is the best profit possible if we sell on that day
# the profit is maximized if we bought the stock at the lowers price on any of the preceding days
def best_profit(prices):
  n = len(prices)
  best = 0
  for i in range(n):
    min_price = min(prices[:i+1])
    best = max(best, prices[i] - min_price)
  return best
print("best profit:", best_profit([3,7,5,1,4,6,2,3]))
print("--------------------------------------------------")
# this algorithm only has one loop but its still not efficient.
# the first for loop scans though all of the elements in the list O(n)
# the function min has to scan through the list once O(n). Like a hidden for loop
# therefore, it also takes O(n^2)
def best_profit_fast(prices):
  n = len(prices)
  best = 0
  min_price = prices[0]
  for i in range(n):
    min_price = min(min_price, prices[i])
    best = max(best, prices[i] - min_price)
  return best
print("best profit:", best_profit_fast([3,7,5,1,4,6,2,3]))
print("--------------------------------------------------")
# we can fix this by computing min_price outside of the for loop making the algorithm O(n) time complex

# Is the algorithm correct
# we can test the algorithm by comparing the brute_force with the simpler correct algorithm
active = False
while True and active == True:
  n = random.randint(1, 20)
  prices = [random.randint(1, 10) for _ in range(n)]

  result_brute = best_profit_brute(prices)
  result_fast = best_profit_fast(prices)

  print(prices, result_brute, result_fast)

  if result_brute != result_fast:
    print("ERROR")
    break
#the matching outputs provide assurance of the correctness of the efficient algorithm.

# Example: Bit string
# You are given a bit string consisting of the characters 0 and 1. How many ways can you select
# two positions in the bit string so taht the left position contains the bit 0 and right contains bit 1
# bit      | 0 1 2 3 4 5 6 7
# position | 0 1 0 0 1 0 1 1
def count_ways(bits):
  n = len(bits)
  result = 0
  for i in range(n):
    for j in range(i + 1, n):
      if bits[i] == "0" and bits[j] == "1":
        result += 1
  return result
print("expected: 12, output:", count_ways(["0","1","0","0","1","0","1","1"]))
print("--------------------------------------------------")
# O(n^2)

def count_ways(bits):
  n = len(bits)
  result = 0
  zeros = 0
  for i in range(n):
    if bits[i] == "0":
      zeros += 1
    if bits[i] == "1":
      result += zeros
  return result
print("expected: 12, output:", count_ways(["0","1","0","0","1","0","1","1"]))
print("--------------------------------------------------")
# the algorithm scans the list in one single loop. Thus, the algorithm runs in O(n) time

# List spliting
# you are given a list containing n integers. Your task is to count how many ways one can split 
# the list into 2 parts so that both parts have the same total sum of elements.
# position | 0  1  2  3  4  5  6  7
# number   | 1 -1  1 -1  1 -1  1 -1
def count_splits(numbers):
  n = len(numbers)
  result = 0
  for i in range(n-1):
    l_sum = sum(numbers[:i+1])
    r_sum = sum(numbers[i+1:])
    if l_sum == r_sum:
      result += 1
  return result
print("expected: 3, output:", count_splits([1,-1,1,-1,1,-1,1,-1]))
print("--------------------------------------------------")
# O(n^2) because going through the list takes O(n) and computing two sums takes O(n)
# O(n) x O(n) = O(n x n) = O(n^2)

def count_splits(numbers):
  n = len(numbers)
  result = 0
  l_sum = 0
  for i in range(n-1):
    l_sum += numbers[i]
    r_sum = sum(numbers[i+1:])
    if l_sum == r_sum:
      result += 1
  return result
print("expected: 3, output:", count_splits([1,-1,1,-1,1,-1,1,-1]))
print("--------------------------------------------------")
# faster than previous but still takes O(n^2) since there is still a sum() being computed inside the
# loop that goes through each element of the list

def count_splits(numbers):
  n = len(numbers)
  result = 0
  l_sum = 0
  total_sum = sum(numbers)
  for i in range(n-1):
    l_sum += numbers[i]
    r_sum = total_sum - l_sum
    if l_sum == r_sum:
      result += 1
  return result
print("expected: 3, output:", count_splits([1,-1,1,-1,1,-1,1,-1]))
print("--------------------------------------------------")
# total sum happens outside the loop (doest change during the loop), therefore it takes O(n) time

# Subtitles
# You are given a list containing n integers. How many ways can we choose a sublist 
# that contains exactly two distinct integers
# ex: [1,2,3,3,2,2,4,2] output: 14

# idx | 0 1 2 3 4 5 6 7
# num | 1 2 3 3 2 2 4 2
# cnt | 0 1 1 1 3 3 2 3
def count_lists(numbers):
  n = len(numbers)
  a = b = -1
  result =  0
  for i in range(1, n):
    if numbers[i] != numbers[i-1]:
      if numbers[i] != numbers[a]:
        b = a
      a = i - 1
    result += a - b
  return  result
print("expected: 14, output:",count_lists([1,2,3,3,2,2,4,2]))