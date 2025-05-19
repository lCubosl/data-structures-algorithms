# You are given a list of integers. Your task is to form as many pairs of integers as possible so that the larger integer of a 
# pair is at least twice the smaller integer of the pair. Each integer can belong to at most one pair.

# To be precise, we say that a pair (a,b) is valid if 2a \le b.

# For example, given the list [4,5,1,4,7,8], at most two such pairs can be formed. One possible solution is to choose the 
# pairs (1,5) and (4,8).

# In a file bigsmall.py, implement a function count_pairs that is given a list of positive integers as a parameter and returns 
# the maximal number of valid pairs.

# You should implement the function so that it runs efficiently even for long lists. The function should finish immediately in 
# the last test case of the code template too.

def count_pairs(numbers):
  hash = sorted(set(numbers))
  count = 0

  if len(hash) <= 1:
    return 0
  
  l, r = 0, len(hash) - 1
  while l <= r:
    if 2 * hash[l] <= hash[r]:
      count += 1
      l += 1
    else:
      r -= 1

  return count


print(count_pairs([1])) # 0
print(count_pairs([1, 2, 3])) # 1
print(count_pairs([1, 2, 3, 4])) # 2
print(count_pairs([1, 1, 1, 1])) # 0
print(count_pairs([10**9, 1, 1, 1])) # 1
print(count_pairs([4, 5, 1, 4, 7, 8])) # 2
print(count_pairs([1, 2, 3, 2, 4, 6])) # 3

numbers = [(x * 999983) % 10**6 + 1 for x in range(10**5)]
print(count_pairs(numbers)) # 41176