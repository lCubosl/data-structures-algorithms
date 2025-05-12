# Consider again the hash function of the earlier task:

# (c_0 A^{n-1} + c_1 A^{n-2} \cdots + c_{n-1} A^0) \bmod M
# The parameters are the same as before: A=23 ja M=2^{32}.

# In a file collision.py, implement the function find_other that takes a string as a parameter and returns a different 
# string with the same hash value.

# The input string consists of the characters a–z and has at most 100 characters. The output string should satisfy the 
# same requirements.

# The function should be efficient and return a different string immediately.
def hash_value(string):
  # you may insert here the code from the earlier task
  pass

def find_other(string):
  pass

string1 = "kissa"
string2 = find_other("kissa")
print(string1, hash_value(string1)) # kissa 2905682
print(string2, hash_value(string2)) # zfgjynuk 2905682

# In the above code, the string zfgjynuk is an example of what the function might return. Your function does not need 
# to return this specific string. It can return any string that satisfies the requirements and has the same hash value.