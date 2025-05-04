#Your task is to pack products into boxes. A given maximum number of products fits in each box. 
# How many boxes is needed at least?

# For example, if there are 10 products and 3 products fit in a box, you need 4 boxes. For instance, 
# you could pack 3, 3, 2 and 2 products into the boxes.
# In a file boxes.py, implement the function min_count that returns the smallest number of boxes needed. 
# The parameters of the function are:

# product_count: the total number of products
# box_size: the number of products that fits in one box

# Your function will be tested using a large number of test cases. In each test case, both parameters 
# are integers in the range 1–100.

def min_count(product_count, box_size):
  res = product_count /  box_size
  return int(res) if res % 2 == 0 else int(res) + 1

  # second option
  if res % 2 == 0:
    return int(res)
  else:
    res = res + 1

  return int(res)

print(min_count(10, 3)) # 4
print(min_count(10, 4)) # 3
print(min_count(100, 1)) # 100
print(min_count(100, 100)) # 1
print(min_count(100, 99)) # 2
print(min_count(5, 5)) # 1
print(min_count(5, 6)) # 1