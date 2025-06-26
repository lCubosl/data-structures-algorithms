# Each element in a sequence of numbers is the smallest positive integer that does not occur earlier in the sequence and that has the same digit 
# in the beginning and in the end.

# The sequence begins as follows:
# 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, ...

# Your task is to compute the number at the position n in the sequence. You may assume that n is at most 1000.
# In a file sequence.py, implement a function generate that returns the number at the given position.

# Only handles 1-18
def generate(n):
  if n / 10 < 1:
    return n
  
  n1 = int(n % 10 + 1)
  
  return f'{n1}{n1}'

# handles all cases
def generate(n):
  sequence = []
  num = 1
  
  while len(sequence) < n:
    s = str(num)
    print(s[-1])
    if s[0] == s[-1]:
      sequence.append(num)
    num += 1
  
  return sequence[n-1]

print(generate(1)) # 1
print(generate(2)) # 2
print(generate(3)) # 3
print(generate(10)) # 11
print(generate(11)) # 22
print(generate(12)) # 33
print(generate(123)) # 1141