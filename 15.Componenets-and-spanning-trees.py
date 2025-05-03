# 15. Components and spanning trees

# Union-find data structure
# maintains a collection of  elements  divided into subsets. initially each element is alone in its own set,
# and then the sets can be repeatedly merged into bigger sets. supports 2 efficient operations
  # find: finds which set has a given  element
  # union: merge 2 sets into a single set

# a union-find data structure is implemented so that one element in each set represents the whole set. all
# other elements contain a reference to the representative element either directly or indiretly through 
# other elements in the set

# conside a union-find data structure for the elements 1,2...,8 the sets are {1,4},{2,5,6},{3,7,8}
union_data_struct = "union-ds-01.png"
# two elements can belong to the same set if they have the same representative.

# when 2 sets are merged, the reference from one of their representatives is set to point to other
# representative.
# the following shows how sets {1,4} and {2,5,6} are merged
union_data_struct02 = "union-ds-02.png"
# the new set becomes {1,2,4,5,6}. the representative 1 siezes to exist. New representative is 5

class UnionFind:
  def __init__(self, nodes):
    self.link = {node: None for node in nodes}
    self.size = {node: 1 for node in nodes}

  def find(self, x):
    while self.link[x]:
      x = self.link[x]
    return x
  
  def union(self, a, b):
    a = self.find(a)
    b = self.find(b)
    if a == b: return

    if self.size[a] > self.size[b]:
      a, b = b, a
    self.link[a] = b
    self.size[b] += self.size[a]

u = UnionFind([1, 2, 3, 4, 5, 6, 7, 8])
u.union(1, 4)
u.union(2, 5)
u.union(5, 6)
u.union(3, 7)
u.union(7, 8)
print(u.find(1)) # 4
print(u.find(2)) # 5
print(u.find(3)) # 7
print(u.find(4)) # 4
print(u.find(5)) # 5
print(u.find(6)) # 5
print(u.find(7)) # 7
print(u.find(8)) # 7
print("--------------------------------------------------")
# {1,4} rep is  4
# {2,5,6} rep is  5
# {3,7,8} rep is  7

# Example: New roads
# bitland  has n cities but initially no roads. your task is to design a class NewRoads with the methods:
  # add_road: adds a road between two cities
  # has_route: checks if the two cities are conencted by roads

class NewRoads:
  def __init__(self, n):
    self.uf = UnionFind(range(1, n+1))
  
  def add_road(self, a, b):
    self.uf.union(a, b)

  def has_route(self, a, b):
    return self.uf.find(a) == self.uf.find(b)
  
# tge idea is that the sets of the union-find data structure correspond to the components of the road
# network. initially, each element is in its own set of size one, which means that each node is in its 
# own component of size one

# add_road calls the method union that merges the components of the graphs
# has_route calls the method find for each element

# time complexity for both add_road and has_route is O(logn)

# Trees in Graphs
# an undirecteed graph is a tree if the graph is connected and acyclic. ex:
tg01 = "trees-in-graphs-01.png"
# unlike trees previously seen, this kind of a tree has no root, and the  nodes have no children or
# parents. however, the tree has leaves, the leaves are the nodes with one connecting edge (exactly)

# when a graph of n nodes is a tree, it has exactly n-1 edges. 
  # if any edge is removes, its no longer connected
  # if any edge is aded, is no longer acyclic

# a spanning tree of a graph is a tree that contains all the nodes of the graph and some subset of 
# the edges.
  # graph on the left
  # spanning tree on the rights
tg2 = "trees-in-graphs-02.png"
# typically a graph has multiple different spanning trees because there are multiple ways of choosing 
# the edges so that the result is a tree

# when the graph is weighed, the weight of a spanning tree is computed as the sum of the weights of 
# its edges. example
tg3 = "trees-in-graphs-03.png"

# Kruskal's Algorithm
# kruskals alg computes a minimum spanning tree of a graph with the help of a union-find data structure.
# the alg goes through the edges in order of weight and selcts an edge to be included in the spanning tree
# if addid it does not create a cycle in the tree

# edge | weight | included in tree?
# 2-3  | 1      | yes
# 1-2  | 2      | yes
# 2-4  | 2      | yes
# 1-3  | 4      | no
# 4-5  | 5      | yes
# 3-5  | 7      | no

# if two edges have the same weight, kruskals alg  can process them in either order
# the union-find data structure is useful for kruskals alg, because it can be used for efficient checking
# if edge should be included or excluded. if the nodes connected by the edge are in different components,
# adding the edge does not create a cycle
class Kruskal:
  def __init__(self, nodes):
    self.nodes = nodes
    self.edges = []

  def add_edge(self, node_a, node_b, weight):
    self.edges.append((node_a, node_b, weight))
  
  def construct(self):
    self.edges.sort(key=lambda x: x[2])

    uf = UnionFind(self.nodes)
    edges_count = 0
    tree_weight = 0

    for edge in self.edges:
      node_a, node_b, weight = edge
      if uf.find(node_a) != uf.find(node_b):
        uf.union(node_a, node_b)
        edges_count += 1
        tree_weight += weight
      
    if edges_count != len(self.nodes) - 1:
      return None
    return tree_weight
  
# construct(): computes minimum spanning tree and returns its weight.
  # first sorts the edge list by weight.
  # then iterates through the edges and selects the edges for the tree using a union-find data-structure

# if a graph is not connected, it has no spanning tree. to detect this, the method counts the edges in the
# tree. if  the count is less than n - 1, the selected edges do not form a tree, which means that the graph
# is not connecnted.
# returns None
  
# implementation
k = Kruskal([1, 2, 3, 4, 5])
k.add_edge(1, 2, 2)
k.add_edge(1, 3, 4)
k.add_edge(2, 3, 1)
k.add_edge(2, 4, 2)
k.add_edge(3, 5, 7)
k.add_edge(4, 5, 5)
print(k.construct()) # 10
print("--------------------------------------------------")