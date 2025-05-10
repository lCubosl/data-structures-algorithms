# Your task is to computer the length distribution of the distinct substrings of a given string.
#For example, the distinct substrings of the string abab are a, b, ab, ba, aba, bab and abab. Their length distribution is as follows:

# length 1: substring count 2
# length 2: substring count 2
# length 3: substring count 2
# length 4: substring count 1

# In a file distribution.py, implement the function create_distribution that returns the distinct substring length distribution for the string given as a parameter. The distribution must be returned as a dictionary as shown in the examples.
# The function will be tested in various situations, where the string is of length at most 20 and consists of the characters a–z. The function should be efficient in all such situations.

def create_distribution(string):
  pass

print(create_distribution("aaaa"))  # {1: 1, 2: 1, 3: 1, 4: 1}
print(create_distribution("abab"))  # {1: 2, 2: 2, 3: 2, 4: 1}
print(create_distribution("abcd"))  # {1: 4, 2: 3, 3: 2, 4: 1}
print(create_distribution("abbbbbb")) # {1: 2, 2: 2, 3: 2, 4: 2, 5: 2, 6: 2, 7: 1}
print(create_distribution("aybabtu")) # {1: 5, 2: 6, 3: 5, 4: 4, 5: 3, 6: 2, 7: 1}