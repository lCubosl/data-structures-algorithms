# Your task is to construct for each level of the tree a list of the nodes on that level in numerical 
# order.

# For example, in the tree below, the top level list is [1], the middle level list is [2,4,5], and the 
# bottom level list is [3,6,7].

# In a file levels.py, implement the function find_levels that takes a reference to the root of a tree as parameter and returns a list whose elements are the level lists.
class Node:
  def __init__(self, value, children=None):
    self.value = value
    self.children = children if children else []

  def __repr__(self):
    if self.children == []:
      return f"Node({self.value})"
    else:
      return f"Node({self.value}, {self.children})"

def find_levels(node):
  levels = []
  find_levels_helper(node, 0, levels)

  return levels

def find_levels_helper(node, depth, levels):
  if len(levels) <= depth:
    levels.append([])

  levels[depth].append(node.value)  

  for child in node.children:
    find_levels_helper(child, depth+1, levels)

tree1 = Node(1, [Node(4, [Node(3), Node(7)]),
                  Node(5),
                  Node(2, [Node(6)])])
print(find_levels(tree1)) # [[1], [2, 4, 5], [3, 6, 7]]

tree2 = Node(1, [Node(2, [Node(3, [Node(4)])])])
print(find_levels(tree2)) # [[1], [2], [3], [4]]

tree3 = Node(1, [Node(2), Node(3), Node(4)])
print(find_levels(tree3)) # [[1], [2, 3, 4]]