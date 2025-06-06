# Consider again the hash function of the earlier task:

# (c_0 A^{n-1} + c_1 A^{n-2} ... + c_{n-1} A^0) mod M
# The parameters are the same as before: A=23 ja M=2^{32}.

# In a file collision.py, implement the function find_other that takes a string as a parameter and returns a different 
# string with the same hash value.

# The input string consists of the characters a–z and has at most 100 characters. The output string should satisfy the 
# same requirements.

# The function should be efficient and return a different string immediately.
import time

def hash_value1(string):
  # O(1)
  hash = {chr(ord("a") + i): i for i in range(26)}
  nums = []
  start_time = time.time()
  # O(n)
  for val in range(1, len(string)+1):
    letter = string[val-1]
    number = hash[letter]
    
    operation = number * 23**(len(string) - val)
    nums.append(operation)

  result = sum(nums)%(2**32)
  end_time = time.time()
  # print("hash_value time:", round(end_time-start_time, 3), "s")
  # total time complexity O(n)
  return result

def hash_value2(string):
  hash = {chr(ord("a") + i): i for i in range(26)}
  MOD = 2**32
  base = 23
  result = 0
  start_time = time.time()
  for val in string:
    result = (result * base + hash[val]) % MOD
  end_time = time.time()
  # print("find_other time:", round(end_time-start_time, 3), "s")
  
  return result

# ----------------------------------------------------------------
import random

def hash_value(string):
  hash = {chr(ord("a") + i): i for i in range(26)}
  nums = []

  for val in range(1, len(string)+1):
    letter = string[val-1]
    number = hash[letter]
    
    operation = number * 23**(len(string) - val)
    nums.append(operation)

  return sum(nums)#%(2**32)

def find_other(string):
  A = 23
  M = 2**32
  target = hash_value(string)
  digits = []

  powers = []
  power = 1

  while power <= target:
    powers.append(power)
    power *= A
  powers.reverse()

  number = target
  for p in powers:
    max_digit = min(25, number // p)
    digit = random.randint(0, max_digit)
    digits.append(digit)
    number -= digit * p
  
  if number != 0:
    return find_other(string)
  
  return ''.join(chr(ord('a') + d) for d in digits)

# print(hash_value1("kissaabcdefghijklmnopqrstuvwxyz")) # 2905682
# print(hash_value2("kissaabcdefghijklmnopqrstuvwxyz")) # 2905682

string1 = "kissa"
string2 = find_other("kissa")
print(string1, hash_value(string1)) # kissa 2905682
print(string2, hash_value(string2)) # zfgjynuk 2905682

# In the above code, the string zfgjynuk is an example of what the function might return. Your function does not need 
# to return this specific string. It can return any string that satisfies the requirements and has the same hash value.