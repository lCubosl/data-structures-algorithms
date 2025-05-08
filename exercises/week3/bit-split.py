# You are given a string where each character is 0 or 1. Your task is to count how many ways the string 
# can be split into two parts so that in both parts the number of 0s is equal to the number of 1s.

# For example, the string 010101 has two valid splits: 01+0101 and 0101+01. In the part 01, both 0 and 1 
# occur once, and in the part 0101, both 0 and 1 occur twice.

# In a file bitsplit.py, implement the function count_splits that takes the list of numbers as a parameter
# and returns the count of valid splits.

# You must implement an efficient solution with a time complexity O(n). For example, you cannot afford to 
# test each possible split position separately.

# In the last test case of the following code template, the string contains 10^5 copies of the string 01. 
# Your function should finish quickly in this test case too.

# O(n^2)
def count_splits(sequence):
  splits = []
  count = 0

  # split string
  for n in range(2, len(sequence) - 1):
    splits.append([sequence[:n],sequence[n:]])

  # early return on empty lists
  if not splits:
    return 0
  
  for l, r in splits:
    if l.count("0") == l.count("1") and r.count("0") == r.count("1"):
      count += 1
  return count

# O(n)
def count_splits(sequence):
  n = len(sequence)
  if n < 4:
    return 0
  
  pre0 = [0] * (n + 1)
  pre1 = [0] * (n + 1)
  
  for i in range(n):
    pre0[i+1] = pre0[i] + (sequence[i] == "0")
    pre1[i+1] = pre1[i] + (sequence[i] == "1")

  total0 = pre0[n]
  total1 = pre1[n]
  count = 0

  for i in range(2, n-1):
    l0 = pre0[i]
    l1 = pre1[i]
    r0 = total0 - l0
    r1 = total1 - l1

    if l0 == l1 and r0 == r1:
      count += 1
  
  return count

print(count_splits("00")) # 0
print(count_splits("01")) # 0
print(count_splits("0110")) # 1
print(count_splits("010101")) # 2
print(count_splits("000111")) # 0
print(count_splits("01100110")) # 3

sequence = "01"*10**5
print(count_splits(sequence)) # 99999