
# A robot moves vertically and horizontally in a grid. Initially the robot moves upwards, and whenever the robot 
# encounters an obstacle, it turns right.

# If the robot eventually moves beyond the edge of the grid, it exits the grid. Otherwise, it continues moving in the 
# grid in an infinite loop.

# Your task is to find out, how many different squares of the grid are visited by the robot, and whether the robot 
# eventually exits the grid or if it stays in an infinite loop.

# In a file roboroute.py, implement the function analyze_route that takes a description of the grid as a parameter. 
# The description is a list of strings, where the character . is a floor square, the character # is an obstacle, and the character R is the initial position of the robot. You may assume that there is only one character  R.

# The function returns a tuple, where the first element is the number of squares on the robot's route, and the second 
# element is True (the robot exits the grid) or False (the robot stays in an infinite loop).

# The function will be tested in various situations, where the size of the grid is at most 20 \times 20 squares. The 
# function should be efficient in all such test cases.

# function expects a "count" with how many squares have been traversed and "exit_grid" to check if it has left the grid
def analyze_route(grid):
  count = 0
  exit_grid = False

  return(count, exit_grid)

# actual function
def analyze_route(grid):
  y = 0
  visited = set()

  for x in range(len(grid)):
    y += 1
    if "R" in grid[x]:
      visited.add((x,y))

    if (4,4) in visited:
      print("True")
          
  return visited

grid1 = [".#......",
          "..#.....",
          ".......#",
          "#.R.....",
          "......#."]
print(analyze_route(grid1)) # (14, True)

grid2 = ["........",
          ".##.....",
          ".......#",
          "#.R.....",
          "......#."]
print(analyze_route(grid2)) # (12, False)

# open link for images on robot routes link: https://cses.fi/dsa25k/task/3464
