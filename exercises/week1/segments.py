# Your task is to divide a string into segments so that each segment is a repeat of the same character. 
# The segments should be represented as a list of pairs containing the segments lengths and characters.\

# For example, the string aaabbccdddd has four segments and can be represented as the list 
# [(3, 'a'), (2, 'b'), (2, 'c'), (4, 'd')].

# In a file segments.py, implement the function find_segments with a string as a parameter. The function 
# returns a list of pairs representing the segments of the string.

# Your function will be tested using many different strings. Each test string consists of the characters
# a–z and contains 1–100 characters.

def find_segments(data):
  res = {}
 
  for x in data:    
    if x not in res:
      res[x] = 0
    res[x] += 1

  return list(res.items())

print("expected: [(3,'a'),(2,'b'),(2,'c'),(4,'d')], output:",find_segments("aaabbccdddd"))
print("expected: [(20,'a')], output:",find_segments("aaaaaaaaaaaaaaaaaaaa"))
print("expected: [(1,'a'),(1,'b'),(1,'c'),(1,'a'),(1,'b'),(1,'c')], output:",find_segments("abcabc"))
print("expected: [(1,'k'),(1,'i'),(2,'s'),(1,'a')], output:",find_segments("kissa"))