# 11. More data structures

# this chapter is about 2 otehr data structures:
  # deque: list structure that supports efficient addition and removal of elements both at the 
  # beggining and end of a list
  # heap: data structure where the smallest or the largest element can be found and removed efficiently

# both data structures are available in python standard library and are thus easy to use

# Deque
# with standard python list, we can efficiently add an element to the end of a list using the method 
# append and remove element from the end of the list using the method pop. 
# however, there is no efficient way of adding or removing an element at the beggining of the list

# deque is a list structure where additions and removals at both ends of the list are efficient. In 
# python, deque is available in module collections and has the following methods:
  # append: add el to end of the list
  # pop: remove el at the end of list
  # appendleft: add el at beggining of list 
  # popleft: remove el at beggining of list 

# in adition to the familiar methods append and pop, we have methods appendleft and popleft taht operate
# at the begining of the list with time complexity of O(1)

import collections

items = collections.deque()

items.append(1)
items.append(2)
items.appendleft(3)
items.append(4)
items.appendleft(5)

print(items)

print(items[0])
print(items[1])
print(items[-1])
print("--------------------------------------------------")
# elements can be accessed using indexing operator [], although its inefficient in a deque, which is a 
# weakness of the deque.
# in the  standard list, any el can be accessed in O(1) time, but an access to an el in the middle of
# deque takes O(n) time

# in python, deque is implemented using linked lists, which enbels the efficient additions and removals 
# at both ends

# Stack and queue
# stack is a data structure that supports adding and removing els at the end of a list. queue is a data 
# structure that supports adding  els to the end of a list and removing els from the beggining of the list\
 
# We can use a deque to implement both a stack and a queue, since operations at both ends are efficient.
# the following implements stack and queue
import collections

class Stack:
  def __init__(self):
    self.stack = collections.deque()

  def push(self, x):
    self.stack.append(x)

  def top(self):
    return self.stack[-1]
  
  def pop(self):
    self.stack.pop()

class Queue:
  def __init__(self):
    self.queue = collections.deque()

  def push(self, x):
    self.queue.append(x)

  def top(self):
    return self.queue[0]
  
  def pop(self):
    self.queue.popleft()
# notice that we could use the standard list to implement a stack as we did in ch.6. however, the
# implementation of a queue benefits from the efficient operations at both ends of a queue

# Heap
# data structure taht only supports adding, accessing and removing elements. Additions to a heap are
# unrestricted, but depending on the implementation of a heap, either only the smallest or only the 
# largest element of the heap can be accessed and removed

# in python, a list can be used as a heap with the following functions in the module "heapq"  
  # heappush(): add element to heap
  # heappop(): remove and return teh smallest element of the heap

# time complexity for both functions is O(logn). In addition, the smallest element in the list is always 
# at the beggining of the list and can be accessed in O(1) time
import heapq

items = []

heapq.heappush(items, 4)
heapq.heappush(items, 2)
heapq.heappush(items, 3)
heapq.heappush(items, 1)
heapq.heappush(items, 5)

print(items)
print(items[0])
heapq.heappop(items)
print(items)
print(items[0])
print("--------------------------------------------------")
# compared to hashing, the advantage of a heap is the efficient access and removal of the smallest
# or largest el. with hashing, this is not possible because hash tables do not store the elements in order
# on the other hand, heap do not support access to any other element other than the largest or smallest.

# heap may contain multiple copies of an element.
import heapq

items = []
heapq.heappush(items, 1)
heapq.heappush(items, 1)
heapq.heappush(items, 1)
print(items)
print("--------------------------------------------------")

# Example: Sliding Window
# you are given a list of n numbers and a parameter k. for each sliding window, i.e, a sublist of $k$
# consecutive elements, from the elft to right, find the smallest element in the sublist
# list=[1,2,3,5,4,4,1,2], k=3, 
# answer is [1,2,3,4,1,1] because:
  # sublists are: [1,2,3],[2,3,5],[3,5,4],[5,4,4],[4,4,1],[4,1,2]
  # smallest el of each list is 1,2,3,4,1,1
import heapq

def find_min(items, k):
  n = len(items)
  heap = []
  res = []

  for i in range(n):
    heapq.heappush(heap, (items[i], i))
    while heap[0][1] <= i - k:
      heapq.heappop(heap)
    if i >= k - 1:
      res.append(heap[0][0])
  
  return res

s = find_min(items=[1,2,3,5,4,4,1,2], k=3)
print("expected: [1,2,3,4,1,1], output:", s)
print("--------------------------------------------------")
# the algorithm iterates through the list and adds pairs of form(x,i) to the heap, where x is the element
# at position i. The smallest element in the heap can be accessed efficiently. If the smallest element is
# outside of the current window, its removed, otherwise teh smallest element is the desired answer for the
# current window

# tiem complexity of O(n x log n)