# You are given a list of page numbers. Your task is to construct a string that describes the page ranges compactly.

# If the list contains all page numbers in the range a \dots b, this should be presented in the form a–b. If the list 
# contains an isolated page number, it should be presented as a single number. If the list contains multiple page 
# ranges, they should be presented as an ordered list separated by commas. Repeated page numbers should be included 
# only once.

# For example, if the list is [3,2,9,4,3,6,9,8], the desired representation is 2-4,6,8-9.

# In a file pages.py, implement the function create_string that takes a list of page numbers as a parameter and 
# returns a string of page ranges as described above.

# You should implement the function so that it does not modify the input list. The last test case in the code template 
# prints the list after calling the function and it should be the same as before the call. The same requirement 
# applies to all tasks this weeks.

def create_string(pages):
  # order set, no repetition
  nums = list(set(pages))
  
  count = 0
  ranges = {}
  ranges[count] = [nums[0]]
  for num in range(1, len(nums)):
    if nums[num]== nums[num - 1] + 1:
      ranges[count].append(nums[num])
    else:
      count +=1
      ranges[count] = [nums[num]]
  
  res = []
  for group in ranges.values():
    if len(group) == 1:
      res.append(str(group[0]))
    else:
      res.append(f"{group[0]}-{group[-1]}")

  return ",".join(res)

print(create_string([1])) # 1
print(create_string([1, 2, 3])) # 1-3
print(create_string([1, 1, 1])) # 1
print(create_string([1, 2, 1, 2])) # 1-2
print(create_string([1, 6, 2, 5])) # 1-2,5-6
print(create_string([1, 3, 5, 7])) # 1,3,5,7
print(create_string([1, 8, 2, 7, 3, 6, 4, 5])) # 1-8
print(create_string([3, 2, 9, 4, 3, 6, 9, 8])) # 2-4,6,8-9

pages = [3, 2, 1, 3, 2, 1]
print(create_string(pages)) # 1-3
print(pages) # [3, 2, 1, 3, 2, 1]