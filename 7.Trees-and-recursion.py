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