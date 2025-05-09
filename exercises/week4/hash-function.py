# Consider the following hash function:
# (c_0 A^{n-1} + c_1 A^{n-2} ... + c_{n-1} A^0) mod M

# The function computes a hash value of a string consisting of the characters c_0,c_1,...,c_{n-1}. Each character 
# is in the range a–z, and the characters have been coded so that a is 0, b is 1 etc.. The function involves two 
# constants with the values A=23 and M=2^{32}.

# For example, when the string is kissa, the function evaluates to
# (10 * 23^4 + 8 * 23^3 + 18 * 23^2 + 18 * 23^1 + 0 * 23^0) mod 2^{32} = 2905682.

# In a file hashing.py, implement the function hash_value that returns the hash value of the string given as a 
# parameter.

def hash_value(string):
  pass    

print(hash_value("abc")) # 25
print(hash_value("kissa")) # 2905682
print(hash_value("aybabtu")) # 154753059
print(hash_value("tira")) # 235796
print(hash_value("zzzzzzzzzz")) # 2739360440