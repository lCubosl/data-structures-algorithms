# Your task is to count how many distinct substrings there are in a given string.

# For example, the string abab has 7 distinct substrings: a, b, ab, ba, aba, bab and abab.

# In a file substrings.py, implement the function count_substrings that returns the number of substrings in the string 
# given as a parameter.

# The function will be tested in various situations, where the string is of length at most 20 and consists of the 
# characters a–z. The function should be efficient in all such situations.

def count_substrings(string):
  pass

print(count_substrings("aaaa")) # 4
print(count_substrings("abab")) # 7
print(count_substrings("abcd")) # 10
print(count_substrings("abbbbbb")) # 13
print(count_substrings("aybabtu")) # 26
print(count_substrings("saippuakauppias")) # 110