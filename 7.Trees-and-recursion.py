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