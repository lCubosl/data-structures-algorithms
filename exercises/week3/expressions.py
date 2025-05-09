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
  # words variables
  letters = []
  temp_word = ""

  # list that stores words
  for char in data:
    if char.isalpha():
      temp_word += char
    else:
      if temp_word:
        letters.append(temp_word)
        temp_word = ""  
  if temp_word:
    letters.append(temp_word)
# --------------------------------------

  # numbers variables
  nums = []
  temp_nums = ""

  # list that stores numbers
  for num in data:
    if num.isdigit():
      temp_nums += num
    else:
      if temp_nums:
        nums.append(int(temp_nums))
        temp_nums = ""  
  if temp_nums:
    nums.append(int(temp_nums))
# --------------------------------------

  res = []

  for word in range(len(letters)):
    if word * 2 + 1 >= len(nums):
      res.append(letters[word])
    elif letters[word] == "add":
      res.append(sum([nums[word*2], nums[(word*2)+1]]))
    elif letters[word] == "mul":
      res.append(nums[word*2] * nums[word*2+1])
    else:
      res.append(letters[word])

  res_str = "".join(str(s) for s in res)
  #print(res_str)

  return res_str

print(evaluate("add(1,20)")) # 21 X
print(evaluate("mul(3,4)")) # 12 X
print(evaluate("aybabtu")) # aybabtu X
print(evaluate("mul(6,7),mul(7,191)")) # 42,1337 X
print(evaluate("abadd(123,456)mulxmul(3,13)")) # ab579mulx39
print(evaluate("mul()mul(13)mul(0,1)")) # mul()mul(13)mul(0,1)

data = "mul(6,7)"*10**5
result = evaluate(data)
print(len(result)) # 200000 X
print(result[:20]) # 42424242424242424242 X

# failed 2 cases
#print(evaluate("abadd(123,456)mulxmul(3,13)")) # ab579mulx39
#print(evaluate("mul()mul(13)mul(0,1)")) # mul()mul(13)mul(0,1)
