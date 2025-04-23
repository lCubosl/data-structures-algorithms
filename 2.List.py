# List in memory
a = 7
b = -3
c = [1, 2, 3, 1, 2]
d = 99

# contents stored in memory starting from adress 100
# 100 101 102 103 104 105 106 107 108 109 110
# 7   -3  1   2   3   1   2   0   0   0   99
# a   b   c                               d
# list "c" only has 5 elements but has 3 aditional memory slots reserved to prepare for possible addition 
# of new elements
# c[2] = addres 102 + 2 = 104

# list operations
# most have the following complexities
# O(1): Opp always efficient
# O(n): Opps efficiency depends on the size of the array
  
# indexing
# items can be accessed and modified using idx opperator []
# O(1)
numbers = [4, 3, 7, 3, 2]
print(numbers[2])
numbers[2] = 5
print(numbers[2])
print("--------------------------------------------------")
