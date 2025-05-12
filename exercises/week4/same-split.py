# You are given a list of integers. Your task is to count how many ways the list can be split into two parts so that 
# every integer on the list occurs both in the left part and in the right part.

# For example, the answer for the list [1,2,1,2,1,2] is 3, because the valid splits are 
# [1,2]+[1,2,1,2], [1,2,1]+[2,1,2] and [1,2,1,2]+[1,2].

# In a file samesplit.py, implement the function count_splits that takes a list as a parameter and returns the number 
# ways to split the list.

# The function should be efficient even for long lists. The last two test cases in the code template are long lists 
# and the function should finish quickly in these cases too.

# O(n^2) because inside of the for loop, numbers arr is being split (additional O(n))
# O(n) x O(n) = O(n x n) = O(n^2)
def count_splits(numbers):
  count = 0
  n = len(numbers)

  for i in range(1, n):
    if set(numbers[:i]) == set(numbers[i:]):
      count += 1
  
  return count

# O(n)
def count_splits(numbers):
  count = 0
  n = len(numbers)

  right_count = {}
  for num in numbers:
    if num in right_count:
      right_count[num] += 1
    else:
      right_count[num] = 1
  
  right_seen = set(right_count.keys())
  left_seen = set()

  for i in range(n):
    num = numbers[i]
    left_seen.add(num)

    right_count[num] -= 1
    if right_count[num] == 0:
      right_seen.remove(num)

    if left_seen == right_seen:
      count += 1
  return count

print(count_splits([1, 1, 1, 1])) # 3
print(count_splits([1, 1, 2, 1])) # 0
print(count_splits([1, 2, 1, 2])) # 1
print(count_splits([1, 2, 3, 4])) # 0
print(count_splits([1, 2, 1, 2, 1, 2])) # 3

numbers = [1, 2] * 10**5
print(count_splits(numbers)) # 199997
numbers = list(range(1, 10**5 + 1)) * 2
print(count_splits(numbers)) # 1