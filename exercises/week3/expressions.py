# You are given a string that contains mathematical expressions of the following forms:

# add(x,y): sum of the numbers x and y
# mul(x,y): product of the numbers x and y

# The numbers x and y are positive integers. You should only process expressions of this precise form.

# Your task is to create a new string where each expression has been replaced with the result of evaluating the 
# expression. For example, the string abadd(123,456)mulxmul(3,13) should turn into the string ab579mulx39.

# In a file addmul.py, implement the function evaluate that takes a string as a parameter and returns the modified 
# string with the expression evaluations.

# Your function should be efficient with long strings too. A good test of efficiency is the last test case in the code 
# template below, where the string contains 10^5 copies of the expression mul(6,7). Your function should finish 
# quickly in this test case too.

def evaluate(data):
  if "add" in data:
    values = [int(char) for char in data if char.isdigit()]
    return sum(values)
  if "mul" in data:
    values = [int(char) for char in data if char.isdigit()]
    return values[0] * values[1]
  return data

print(evaluate("add(1,2)")) # 3
print(evaluate("mul(3,4)")) # 12
print(evaluate("aybabtu")) # aybabtu
print(evaluate("mul(6,7),mul(7,191)")) # 42,1337
print(evaluate("abadd(123,456)mulxmul(3,13)")) # ab579mulx39
print(evaluate("mul()mul(13)mul(0,1)")) # mul()mul(13)mul(0,1)

#data = "mul(6,7)"*10**5
#result = evaluate(data)
#print(len(result)) # 200000
#print(result[:20]) # 42424242424242424242