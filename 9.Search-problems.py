# 9. Search Problems

# many algorithmic problems can be thought of as search problems, where we have a set of possible 
# solutions and the goal is to find an optimal solution or to count the number of desired solutions

# a straightforward way of solving seach problems is a brute force one that goes through all possible
# solutions one by one. This method always creates the correct answer but the search may take too long 
# to be practical if the number of solutions is big

# if the goal is to find an optimal solutions, there may be a greedy alg that constructs a solution
# efficiently following a certain logic without going through all possibilities. However, a greedy 
# algorithm might not find an optimal solution

# a more advanced method for search problem is dynamic programming, which can be used both for finding
# an optimal solution and for counting solutions.


# Iretating Solutions
# a brute force algorithm for a search problem iterates through all possible solutions one by one. During
# the iteration, the alg can select solutions that satisfy certain conditions or are optimal in some way.

# a brute force algorithm can be implemented to construct all solutions by combining given elements in a
# certain way. 

# Sequences
# the input consists of n elements and we want all sequences of m elements. There are n^m such sequences

# if elements are [1,2,3] and m=2, the sequences are [1,1],[1,2],[1,3],[2,1],[2,2],[2,3],[3,1],[3,2],[3,3]
import itertools

for repetition in itertools.product([1,2,3], repeat=2):
  print(repetition)
print("--------------------------------------------------")
# or (only for repeat 2)
arr = [1,2,3]

for i in arr:
  for j in arr:
    print((i, j))
print("--------------------------------------------------")
# or (general works for any repeat)
def manual_product(arr, repeat, prefix=None):
  if prefix is None:
    prefix = []

  if repeat == 0:
    print(tuple(prefix))
    return

  for item in arr:
    manual_product(arr, repeat-1, prefix+[item])

manual_product([1,2,3], 2)
print("--------------------------------------------------")