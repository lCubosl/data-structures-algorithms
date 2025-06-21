# Your task is to build a list that contains the subtree sizes for all the nodes in a tree from the smallest to the largest.

# For example, in the tree below, the desired list is [1, 1, 1, 1, 2, 3, 7].

# The tree has four leaves with a subtree size of 1. The node 2 has a subtree of size 2, the node 4 has a subtree of size 3, 
# and the node 1 has a subtree of size 7.

# In a file subtrees.py, implement the function count_subtrees that takes a reference to the root of a tree as parameter and 
# returns the list of subtree sizes.

class Node:
  def __init__(self, value, children=None):
    self.value = value
    self.children = children if children else []

  def __repr__(self):
    if self.children == []:
      return f"Node({self.value})"
    else:
      return f"Node({self.value}, {self.children})"

def count_subtrees(node):
  subtrees = []
  subtrees_helper(node, subtrees)

  return sorted(subtrees)
  
def subtrees_helper(node, subtrees):
  count = 1

  for child in node.children:
    count += subtrees_helper(child, subtrees)
  subtrees.append(count)
  return count



tree1 = Node(1, [Node(4, [Node(3), Node(7)]),
                  Node(5),
                  Node(2, [Node(6)])])
print(count_subtrees(tree1)) # [1, 1, 1, 1, 2, 3, 7]

tree2 = Node(1, [Node(2, [Node(3, [Node(4)])])])
print(count_subtrees(tree2)) # [1, 2, 3, 4]

tree3 = Node(1, [Node(2), Node(3), Node(4)])
print(count_subtrees(tree3)) # [1, 1, 1, 4]