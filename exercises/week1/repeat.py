# Your task is to find out how long is the shortest string that forms the given string when repeated. For example, when the input string is 
# abcabcabcabc, the shortest repeating string is abc.

# The string consists of the characters a–z and contains at most 100 characters.

# In a file repeat.py, implement a function find that returns the length of the shortest repeating string.

def find(s):
  string_list = [char for char in s]
  n = len(string_list)

  for i in range(1, n + 1):
    if n % i == 0:
      if string_list[:i] * (n // i) == string_list:
        return i
  
  return n    

print(find("aaa")) # 1
print(find("abcd")) # 4
print(find("abcabcabcabc")) # 3
print(find("aybabtuaybabtu")) # 7
print(find("abcabca")) # 7