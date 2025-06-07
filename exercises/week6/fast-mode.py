# Implement the class FastMode with the following methods:

# add(x, k): add the number x to the list k times
# mode(): return the mode of the list, i.e., the most frequent element (if there are multiple modes, return the smallest of them)

# The time complexity of both methods should be O(1).
# In a file fastmode.py, implement a class FastMode according to the following template:

# O(n) gets the entire list when we only want the highest frequency number
class FastMode:
  def __init__(self):
    self.numbers = []
    self.times = 0

  def add(self, x, k):
    self.times = k
    self.numbers.extend([x] * k)

  def mode(self):
    return self.numbers

m = FastMode()
m.add(4, 7)
print(m.mode()) # 4
m.add(8, 5)
print(m.mode()) # 4
m.add(8, 3)
print(m.mode()) # 8
m.add(4, 1)
print(m.mode()) # 4

# dictionary aproach
class FastMode:
  def __init__(self):
    self.numbers =  {}
    self.value = None
    self.frequency = 0

  def add(self, x, k):
    self.numbers[x] = self.numbers.get(x, 0) + k

    if self.numbers[x] > self.frequency:
      self.frequency = self.numbers[x]
      self.value = x

  def mode(self):
    return self.value

m = FastMode()
m.add(4, 7)
print(m.mode()) # 4
m.add(8, 5)
print(m.mode()) # 4
m.add(8, 3)
print(m.mode()) # 8
m.add(4, 1)
print(m.mode()) # 4