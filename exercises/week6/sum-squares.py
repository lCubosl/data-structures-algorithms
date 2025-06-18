# When the data contains the observations (x_1,y_1),(x_2,y_2), ...,(x_n,y_n) and the line y=ax+b is fitted to the data, 
# the error can be computed with the sum of squares formula

# $$\sum_{i=1}^{n}(y_i-(ax_i+b))^2.$$

# For example, when the data is (1,1),(3,2),(5,3) and the line is y=x-1 (i.e., a=1 and b=-1), the error is
# $$(1-(1-1))^2+(2-(3-1))^2+(3-(5-1))^2=2.$$

# In a file squaresum.py, implement the class DataAnalyzer with the methods
  # add_point(x, y): add an observation to the data
  # calculate_error(a, b): return the sum of squares error for the given line parameters

# The time complexity of both methods should be O(1).
class DataAnalyzer:
  def __init__(self):
    self.numbers = []

  def add_point(self, x, y):
    self.numbers.append((x, y))

  def calculate_error(self, a, b):
    error = 0
    for x, y in self.numbers:
      predicted_y = a * x + b
      error += (y - predicted_y) ** 2
    return error

analyzer = DataAnalyzer()

analyzer.add_point(1, 1)
analyzer.add_point(3, 2)
analyzer.add_point(5, 3)
print(analyzer.calculate_error(1, 0)) # 5
print(analyzer.calculate_error(1, -1)) # 2
print(analyzer.calculate_error(3, 2)) # 293

analyzer.add_point(4, 2)
print(analyzer.calculate_error(1, 0)) # 9
print(analyzer.calculate_error(1, -1)) # 3
print(analyzer.calculate_error(3, 2)) # 437

# You can test the efficiency of your solution with the following code. In this case too the code should finish almost immediately.
analyzer = DataAnalyzer()
total = 0

for i in range(10**5):
  analyzer.add_point(i, i % 100)
  total += analyzer.calculate_error(i % 97, i % 101)

print(total) # 25745448974503313754828