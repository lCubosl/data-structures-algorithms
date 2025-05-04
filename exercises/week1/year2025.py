# The year 2025 is special because (20+25)^2=2025, i.e., the the year is the square of the sum of its 
# first and second halves.

# In a file special.py, implement the function check_year that reports if the given year is special. 
# The function should return True or False.

# Your function will be testes using many different test cases. In each test case, the year is in the 
# range 1000–9999.

def check_year(year):
  split = list(str(year))
  half1 = "".join(split[:2])
  half2 = "".join(split[2:])
  
  if (int(half1) + int(half2))**2 == year:
    return True
  else:
    return False

print("Output:",check_year(1995), "expected: false") 
print("Output:",check_year(2024), "expected: false") 
print("Output:",check_year(2025), "expected: true") 
print("Output:",check_year(2026), "expected: false") 
print("Output:",check_year(3025), "expected: true") 
print("Output:",check_year(5555), "expected: false") 