# 12. Binary Search Tree
# BST is a data structure that maintains a set of elements. The basic operations are the same as with
# hashing: elements can be added, searcheed and removed efficiently

# bst differs from hashing in that it maintians the elemetns in order. because of this, the smallest
# and the largest element in the set can be found efficiently, which is not possible with hashing

# the python standard library does not have an implementation of a bst, which makes using them a little 
# bit more difficult. we will set our own.

# Set a binary search tree

# a binary search tree is a binary tree, where each node stores one element of the set. the follwoing 
# corresponds to a bst of the set {2,3,5,7,8,9}
bst = "bst01.png"

# organized so that for every node, 
  # the elements in the left are smaller than the element in the node
  # the elements in the right are larger than the element in the node

# the element locations can be chosen freely as long as the above ordering condition is satisfied by 
# every node. thus the same set can be represented by different bst. the following 2, both represent the 
# set {1,2,3,4,5}
bst2 = "bst02.png"

# Finding an element
# when seaching for an element, we start at the root. If the element in the root node is smlaler than th
# query element, the search continues in the right subtree, otherwise the element shifts continues to the
# left subtree.
# this continues until we find the element, or until there is no child in the direction where the seatch
# should continue

# seach route to find element 7
bst3 = "bst03.png"

# Adding an element
# when adding an element, the first stage is to search for the element in the set. If its found, no 
# addition is performed. If its not found, a new node is inserted where the seach would have continued

# addition of the element 4
bst4 = "bst04.png"

# Removing an element
# when removing an element: 
  # first step is to find the node containing it.
  # if node has no children:
    # node is removed
  # if node has one child:
    # node is removed and replaced by child
  # if node has two children:
    # find the successor of eleemnt, and swap the elements  in the two  nodes. then the new node of the 
    # element can be removed, because it has at most, 1 child

# images shows example, where we want to remove element 5. since the node with element 5 has 2 children, 
# 5 is swapped with its successor 7. then the new node of  the element 5  is easy to remove because it has
# no children
bst5 = "bst05.png"

# Implementation in Python
# implementation of a binary search tree in python 

# class Node stores the information related to a node in the tree
class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

# class tree set implements the binary search tree
class  TreeSet:
  def __init__(self):
    self.root = None
  
  # add elements to the set
  def add(self, value):
    if not self.root:
      self.root = Node(value)
      return
  
    node = self.root
    while True:
      if node.value == value:
        return
      if node.value > value:
        if not node.left:
          node.left = Node(value)
          return
        node = node.left
      else:
        if not node.right:
          node.right = Node(value)
          return
        node = node.right

  # finds element is in the set using the method __contains__
  def __contains__(self, value):
    if not self.root:
      return False
    
    node = self.root
    while node:
      if node.value == value:
        return True
      if node.value > value:
        node = node.left
      else:
        node = node.right
    return False
  
  # string representation using __repr__ to construct a string representing the set
  def __repr__(self):
    items = []
    self.traverse(self.root, items)
    return str(items)
  
  def traverse(self, node, items):
    if not node:
      return
    self.traverse(node.left, items)
    items.append(node.value)
    self.traverse(node.right, items)
  # mehtod __repr__ uses the method traverse that visits all nodes of the tree and adds their elements 
  # to the list.
    # first: visits all nodes in the left
    # second: adds all found elements to the node list
    # third: visits all nodes in the right subtree
  # ensuring all nodes are in order of value

s = TreeSet()

s.add(1)
s.add(2)
s.add(3)

print(2 in s) # True
print(4 in s) # False

print(s) # [1, 2, 3]
print("--------------------------------------------------")

# Balanced trees
# time complexity of a tree can be stated as O(h) since the length of the longest possible rout is equal
# to the height of the tree

# height of the tree can be O(n) since it can tall if there is a single chain 1,...,n making the heigh
# n - 1 (aka O(n))

# its possible to implement a bst so that the elements are distributed evenly across the tree and the 
# height is always of order log n. such a tree is called balanced (time complexity O(log n))

# Example: Hotel
# a hotel has n rooms, each of which has a certain capacity (number of people). the hotel recieves m 
# groups of visitors. your task is to proccess the group of the smallest room with sufficient capacity for
# the whole group or report that no suitable room is available

# room_capacity=[2,4,4,8], group_size=[4,6,2,5,2], answer=[4,8,2,0,4] (0 means  no room was assigned) 
  # g1 gets 4
  # g2 gets 8
  # g3 gets 2
  # g4 does not get a room
  # g5 gets 4 

def find_rooms(sizes, requests):
  rooms = TreeSet()
  counter = 0
  for size in sizes:
    counter += 1
    rooms.add((size, counter))

  res = []
  for request in requests:
    room = rooms.next((request, 0))
    if room == None:
      res.append(0)
    else:
      rooms.remove(room)
      res.append(room[0])
  
  return res