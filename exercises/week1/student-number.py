# A University of Helsinki student number is a sequence of nine digits. The first digit is 0 and the 
# last digit is a check value that allows checking for typos in the student number.

# The check value is obtained by summing up the other digits multiplied by the values 3,7,1,3,7,1,3,7 in 
# the left-to-right order. If the sum is a multiple of 10, the check digit is 0. Otherwise, the check 
# digit is the distance of the sum to the next multiple of 10.

# For example, if the student number is 012749139, the sum is 3.0+7.1+1.2+3.7+7.4+1.9+3.1+7.3=91. 
# The next multiple of 10 is 100 and the distance to that is 9. Thus the last digit of the student 
# number is 9.

# In a file student.py, implement the function check_number that reports if the parameter is a valid
# student number. The function should return True or False.

# Your function will be tested using many different sequences of digits.

def check_number(number):
  temp = 0
  key = [3,7,1,3,7,1,3,7]
  split = list(str(number))

  if split[0] != "0":
    return False
  
  if len(split) > 9:
    return False

  for i in range(len(split) - 1):
    temp += int(split[i]) * key[i]

  distance = (10 - (temp % 10)) % 10
  if distance != int(split[-1]):
    return False
  return True

print("expected: false, output:",check_number("012749138")) # False
print("expected: true, output:",check_number("012749139")) # True
print("expected: true, output:",check_number("013333337")) # True
print("expected: false, output:",check_number("012345678")) # False
print("expected: true, output:",check_number("012344550")) # True
print("expected: false, output:",check_number("1337")) # False
print("expected: false, output:",check_number("0127491390")) # False