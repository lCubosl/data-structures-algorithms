# Trees and recursion
# A tree is a data structure that consists of node at different levels.
# A tree can represent a hierarchy thorugh connections between
# nodes of different levels

image = "tree-map.png"
# the tree has seven nodes at 3 levels
# top node: root
# child node: lower level node connected to root
# leaf node: node with no children

# every node except leaf has one parent. This means that any node can be
# reached from the root by following the node connections downwards.

# subtree of a node consists of all nodes that can be reached by following
# connections downwards from the node. the root has no parent

# the depth of a node tells how low the node is in the tree. The depth of the
# root is 0. The depth of other node is bigger that that of its parent
  # depth of root : 0
  # depth of 4: 1
  # depth of 3: 2

# the height of the tree is the maximum depth of any node in the tree.
# ex "tree-map.png": depth 2 - nodes 3, 7

# Implementing a tree
class Node:
  def __init__(self, value, children=[]):
    self.value = value
    self.children = children
  
  def __repr__(self):
    return str(self.value)
# list is empty by default.
# constructor __init__ takes 2 parameters:
  # value stored in the node
  # list of children
# the following creates three nodes so that  2 and 3 are children of 1
node2 = Node(2)
node3 = Node(3)
node1 = Node(1, [node2, node3])
node = Node(1)
print(node)
print("--------------------------------------------------")

# with this class, we can define a tree by building the root node of the tree.
# the code bellow creates the tree "tree-map.png"
tree = Node(1, [Node(4, [Node(3), Node(7)]),
                Node(5),
                Node(2, [Node(6)])])

# Traversing a tree
# A natural way to process a tree is using recursion. For example, the following
# functioon traverse goes through all the nodes taht are in the subtree of
# the node
def traverse(node):
  print(node)
  for child in node.children:
    traverse(child)

tree = Node(1, [Node(4, [Node(3), Node(7)]),
                Node(5),
                Node(2, [Node(6)])])

traverse(tree)
print("--------------------------------------------------")
# the function traverse starts by printing the value (node.value) of the given node.
# then the function iterates through the children of the node (node.children)
# and calls itself recursively for each child

# we can further illustrate the operation of the function with the following
# modifications
def traverse(node):
  print("enter", node.value)
  for child in node.children:
    traverse(child)
  print("leave", node.value)

  tree = Node(1, [Node(4, [Node(3), Node(7)]),
                Node(5),
                Node(2, [Node(6)])])

traverse(tree)
print("--------------------------------------------------")

# Computing information from a tree
# trees are ofter processed using recursive funtions that compute some value 
# related to a tree.
# count_nodes counts how many nodes are in the subtree of hte node "node"

def count_nodes(node):
  result = 1
  for child in node.children:
    result += count_nodes(child)
  return result

tree = Node(1, [Node(4, [Node(3), Node(7)]),
                Node(5),
                Node(2, [Node(6)])])

print(count_nodes(tree))
print("--------------------------------------------------")
# the function computes the node count into the variable result.
# initial value of the var is 1, because it includes the node itself.
# then, the function goes through the children of the node and 
# recusively counts nodes in the subtrees of the children

image = "tree-map.png"
# using this image as an example, the variable is initialized with 1,
# then, the node counts the node children added to it (4,5,2).
# then, the subtree of 4, has 3
# 5 has 1
# subtree 2 has 2
# 1(1) + 3(4,5,2) + 2(3,7) + 1(6) = 7
# we can further illustrate using the following:
def count_nodes(node):
  result = 1
  for child in node.children:
    result += count_nodes(child)
  print("subtree of node", node, "has", result, "nodes")
  return result

tree = Node(1, [Node(4, [Node(3), Node(7)]),
                Node(5),
                Node(2, [Node(6)])])

count_nodes(tree)
print("--------------------------------------------------")

# other values related to trees can be computed using the same aproach.
# define some vars, iterate through children recursively, and update vars

# the following function computes height of the tree (max depth of any node).
def count_height(node):
  result = 0
  for child in node.children:
    result = max(result, count_height(child) + 1)
  print(result)
  return result

tree = Node(1, [Node(4, [Node(3), Node(7)]),
                Node(5),
                Node(2, [Node(6)])])

count_height(tree)
print("--------------------------------------------------")

# Computing dephts
# sometime it is useful to add a param to the recursive funtion to keep
# track of the depth of a node
# the following function prints out the depth of every node
def traverse(node, depth):
  print("node:", node, "depth:", depth)
  for child in node.children:
    traverse(child, depth + 1)

tree = Node(1, [Node(4, [Node(3), Node(7)]),
                Node(5),
                Node(2, [Node(6)])])

traverse(tree, 0)
print("--------------------------------------------------")

# lets design a more complicated function get_depths that returns the 
# node depths as a list ordered from the smallest to the biggest depth.
# with the example tree, the function should return the list [0,1,1,1,2,2,2]
# a good way to implement a function like this is to define a helper
# function that has more parameters
def get_depths(node):
  depths = []
  get_depths_helper(node, 0, depths)
  return sorted(depths)

def get_depths_helper(node, depth, depths):
  depths.append(depth)
  for child in node.children:
    get_depths_helper(child, depth + 1, depths)
  
tree = Node(1, [Node(4, [Node(3), Node(7)]),
                Node(5),
                Node(2, [Node(6)])])

print(get_depths(tree))
print("--------------------------------------------------")
# function creates a list depths for storing the depths. then the function calls the helper function that 
# adds all the depths to the lists. FInally the function get_depths sorts and returns the list

# another way to implement the two functions.
def get_depths(node):
  return sorted(get_depths_helper(node, 0))

def get_depths_helper(node, depth):
  depths = [depth]
  for child in node.children:
    depths += get_depths_helper(child, depth + 1)
  return depths

tree = Node(1, [Node(4, [Node(3), Node(7)]),
                Node(5),
                Node(2, [Node(6)])])

print(get_depths(tree))
print("--------------------------------------------------")
# now the function get_depths_helper creates a list initialy containg the depth of the current node.
# then the function computes the lists for the child subtrees recusively and adds those lists into its own
# "get_depths" get the list of depths from the helper func and returns it in sorted order

# Improving the class

class Node:
  def __init__(self, value, children=[]):
    self.value = value
    self.children = children
  
  def __repr__(self):
    return str(self.value)
# as we have seen, the class works well in many cases, but there is feature of python that can cause
# problems in some cases. Lets see the example bellow
node1 = Node(1)
node2 = Node(2)

node1.children.append(node2)

print(node1.children)
print(node2.children)
print("--------------------------------------------------")
# created 2 nodes and add node 2 as child of node 1. This has the effect of adding the node 2 as
# its own child too.
# this is because of the defualt parameter [] which is created once and shared between all calls
# of the method.Both nodes refer to the same empty list and any additions are seen by both nodes

# fix
class Node:
  def __init__(self, value, children=None):
    self.value = value
    self.children = children if children  else []
  
  def __repr__(self):
    return str(self.value)
  
node1 = Node(1)
node2 = Node(2)

node1.children.append(node2)

print(node1.children)
print(node2.children)
print("--------------------------------------------------")

# issue 2: printing a node, prints only the value and no information about the children
tree = Node(1, [Node(2), [Node(3), Node(4)], Node(5)])
print(tree)
print("--------------------------------------------------")

# __repr__ should return a string that can be used for constructing the object. This is not the case with
# the above method __repr__

# fix:
class Node:
  def __init__(self, value, children=None):
    self.value = value
    self.children = children if children else []
  
  def __repr__(self):
    if self.children == []:
      return f"Node({self.value})"
    else:
      return f"Node({self.value}, {self.children})"
    
tree = Node(1, [Node(2), [Node(3), Node(4)], Node(5)])
print(tree)
print("--------------------------------------------------")

# Example: Employes
# Trees can be used for representing hierarchical structures. Ex, the personel structure of an organization
# could be represented as a tree, where each employee is a node, and the children of the node are 
# the subordinates of the employee
# the following class can be used for storing the name of an employee and a list of the 
# employees subordinates.
class Employee:
  def __init__(self, name, subordinates=[]):
    self.name = name
    self.subordinates = subordinates
  
  def __repr__(self):
    return self.name
  
def list_employees(employee, level=0):
  print(" "*(level*4), employee)
  for subordinate in employee.subordinates:
    list_employees(subordinate, level + 1)

staff = Employee("Emilia",
                 [
                   Employee("Antti"),
                   Employee("Leena", [Employee("Jussi")]),
                   Employee("Matti", [Employee("Sasu")])
                 ])

list_employees(staff)
print("--------------------------------------------------")

# Example: Queens
# a systematic iteration of possible solution to a problem can often be seen as a long traversal of a tree.
# this technique of solving a problem is known as backtracking. Let us consider the following problme

# how many ways can you place n queens on an n x n chess board so that no two queens attack each other?
# two queens attack each other if they are on the same row, col or diagonal

# ex: n = 4, there are 2 solutions
# - Q - -     - - Q -
# - - - Q     Q - - -
# Q - - -     - - - Q
# - - Q -     - Q - -

# we can solve the task by traversing a tree, where the root represents the empty board. Each non-root
# node represents a board obtained by modifying the board of its parent by adding one more queen to an 
# empty row.
# by traversing the board, we will find all valid solutions
queens = "queens-tree-map.png"

def count_queens(n):
  return count(n, 0, [])

def count(n, row, queens):
  if row == n:
    return 1
  result = 0
  for col in range(n):
    attacks = [attack(queen, (row, col)) for queen in queens]
    if not any(attacks):
      result += count(n, row + 1, queens + [(row, col)])
  return result

def attack(queen1, queen2):
  if queen1[0] == queen2[0] or queen1[1] == queen2[1]:
    return True
  if abs(queen1[0] - queen2[0]) == abs(queen1[1] - queen2[1]):
    return True
  return False

print(count_queens(4))
print(count_queens(8))
print("--------------------------------------------------")
# count: 3 parameters - size of the board(n), the empty row, the list of queens already placed in the board
# rows and cols are numbered 0, n-1. Queens represented as pairs (x: column,y: row)
# function goes through all the cols, checks if a new queen can be placed at the col without attacking
# other queens. If it can, precesses that placement recursively

# attack handles attack checks. 
# The 1st condition checks if queens are in the same row/col
# 2nd condition checks if queens attack each other diagonaly
# The function any in the code returns True if the given list contains True at least  once.
# "not any(attacks)" menas that the list attacks contains only False values, that the new queen attacks 
# none of the previously placed queens