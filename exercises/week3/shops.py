# You are given a string that describes a row of buildings on a street. Each character is either 0 (house) or 1 (shop).

# Your task is to construct a list that tells for each building, what is the shortest distance from the building to a shop. If the 
# building is a shop, the distance is 0.

# For example, if the buildings are 00100010, the desired list is [2,1,0,1,2,1,0,1]. If the buildings are 00100000, the list is 
# [2,1,0,1,2,3,4,5]. You may assume that at least one of the buildings is a shop.

# In a file shops.py, implement the function find_distances that takes a building descriptor string as a parameter and returns the 
# list of distances.

# You must implement an efficient solution with a time complexity O(n). Your function should finish quickly even with the last test 
# case of the code template.

def find_distances(street):
  n = len(street)
  distances = [float("inf")] * n

  for num in range(n):
    if street[num] == "1":
      distances[num] = 0
    elif num > 0 and distances[num-1] != float("inf"):
      distances[num] = distances[num - 1] + 1
  
  for num in range(n-1,-1,-1):
    if street[num] == "1":
      distances[num] = 0
    elif num < n - 1 and distances[num+1] != float("inf"):
      distances[num] = min(distances[num], distances[num + 1] + 1)

  return distances
    

print(find_distances("00100010")) # [2, 1, 0, 1, 2, 1, 0, 1]
print(find_distances("00100000")) # [2, 1, 0, 1, 2, 3, 4, 5]
print(find_distances("11111111")) # [0, 0, 0, 0, 0, 0, 0, 0]
print(find_distances("01010101")) # [1, 0, 1, 0, 1, 0, 1, 0]
print(find_distances("10000000")) # [0, 1, 2, 3, 4, 5, 6, 7]
print(find_distances("00000001")) # [7, 6, 5, 4, 3, 2, 1, 0]

n = 10**5
street = "0"*n + "1" + "0"*n
distances = find_distances(street)
print(distances[1337]) # 98663