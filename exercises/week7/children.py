# Your task is to build a list that contains the child counts of all the nodes in a tree from the smallest to the largest.

# For example, in the tree below, the desired list is [0, 0, 0, 0, 1, 2, 3]. The tree has four nodes that have no children. 
# The node 2 has one child, the node 4 has two children, and the node 1 has three children.

# In a file children.py, implement the function count_children that takes a reference to the root of a tree as parameter and 
# returns the list of child counts.

class Node:
  def __init__(self, value, children=None):
    self.value = value
    self.children = children if children else []

  def __repr__(self):
    if self.children == []:
      return f"Node({self.value})"
    else:
      return f"Node({self.value}, {self.children})"

# original function to get depths, store them in a list and sort them  
# def get_depths(node):
#   depths = []
#   get_depths_helper(node, 0, depths)
#   return sorted(depths)

# def get_depths_helper(node, depth, depths):
#   depths.append(depth)
#   for child in node.children:
#     get_depths_helper(child, depth + 1, depths)
  
# tree = Node(1, [Node(4, [Node(3), Node(7)]),
#                 Node(5),
#                 Node(2, [Node(6)])])

def count_children(node):
  counts = []
  dfs(node, counts)

  return sorted(counts)

def dfs(node, counts):
  counts.append(len(node.children))
  for child in node.children:
    dfs(child, counts)


tree1 = Node(1, [Node(4, [Node(3), Node(7)]),
                  Node(5),
                  Node(2, [Node(6)])])
print(count_children(tree1)) # [0, 0, 0, 0, 1, 2, 3]

tree2 = Node(1, [Node(2, [Node(3, [Node(4)])])])
print(count_children(tree2)) # [0, 1, 1, 1]

tree3 = Node(1, [Node(2), Node(3), Node(4)])
print(count_children(tree3)) # [0, 0, 0, 3]