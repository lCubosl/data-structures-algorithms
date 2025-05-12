# You are given a play list, where each song is represented by an integer. Your task is to count how many sublists 
# contain no song twice.

# For example, the sublists of the play list [1,2,1,3] are [1], [2], [1], [3], [1,2], [2,1], [1,3], [1,2,1], [2,1,3] 
# and [1,2,1,3]. For instance, the sublist [1,3] is valid as is contains each of the songs 1 and 3 once only. The sublist [1,2,1] is not valid as it contains the song 1 twice.

# The desired answer for the play list is 8, because the valid sublists are [1], [2], [1], [3], [1,2], [2,1], [1,3] 
# and [2,1,3]. Notice that the sublist [1] is counted twice since it occurs twice in the play list.

# In a file playlist.py, implement the function count_parts that takes a play list as a parameter and returns the 
# number of valid sublists.

# The function should be efficient even for long lists. The last two test cases in the code template are long lists 
# and the function should finish quickly in these cases too.

# O(n^2)
def count_parts(songs):
  seen = {}
  count =  0

  for i in range(len(songs)):
    for j in range(i, len(songs)):
        sublist = tuple(songs[i:j+1])
        if len(sublist) == len(set(sublist)):
          seen[count] = sublist
          count += 1
  
  return len(seen)

# sliding window
def count_parts(songs):
  seen = set()
  left = 0
  count =  0

  for right in range(len(songs)):
    while songs[right] in seen:
      seen.remove(songs[left])
      left += 1
    seen.add(songs[right])
    count += (right - left + 1)
  
  return count

print(count_parts([1, 1, 1, 1])) # 4
print(count_parts([1, 2, 3, 4])) # 10
print(count_parts([1, 2, 1, 2])) # 7
print(count_parts([1, 2, 1, 3])) # 8
print(count_parts([1, 1, 2, 1])) # 6

#songs = [1, 2] * 10**5
#print(count_parts(songs)) # 399999
#songs = list(range(1, 10**5 + 1)) * 2
#print(count_parts(songs)) # 15000050000