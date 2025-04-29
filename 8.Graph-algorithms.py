# 8. Graph algorithms

# graph is a data structure that consists of nodes and edges. Each edge connects 2  nodes.
# the following graph has five nodes and 7 edges
graph = "graph.png"
# a neighbor of node is another node connected to it by an edge. 
# in the example, node 1 has 2,3 and 4 as neighbours. Degree of node is the number of its neighbors.
# degree of 1 is 3 (3 neighbours: 2,3,4)

# path between nodes is a route along thte edges of the graph.
# List of possible paths 1 to 5:
# 1 -> 2 -> 5
# 1 -> 4 -> 5
# 1 -> -> 3 -> 4 -> 5
# 1 -> -> 3 -> 2 -> 4 -> 5

# graph aplications:
# road network: nodes are cities, edges are roads. Path between roads is route between cities
# contact network: nodes are people and the edges are contacts.
# communication network: nodes are computes, edges are connections.

# Programing with graphs
# a common way to represent a graph in programming is to have an adjacency list for each notde.
# the adjacency list of a node x contains all nodes connected to x by an edge
# In python, we store graphs using dictionary as follows:
graph = {
  1: [2,3,4],
  2: [1,4,5],
  3: [1,4],
  4: [1,2,3,5],
  5: [2,4],
}
# is often useful to define a class for graphs with a method for adding edges.
class Graph:
  def __init__(self, nodes):
    self.nodes = nodes
    self.graph = {node: [] for node in nodes}
  
  def add_edge(self, a, b):
    self.graph[a].append(b)
    self.graph[b].append(a)

g = Graph([1,2,3,4,5])

g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(1,4)
g.add_edge(2,4)
g.add_edge(2,5)
g.add_edge(3,4)
g.add_edge(4,5)

# DFS Depth-first Search
# DFS is a technique for iterating through all nodes of a graph that can be reached from a given 
# initial  node by following edges. DFS can be implemented using  recursion given the adjacency lists
class DFS:
  def __init__(self, nodes):
    self.nodes = nodes
    self.graph = {node: [] for node in nodes}

  def add_edge(self, a, b):
    self.graph[a].append(b)
    self.graph[b].append(a)

  def visit(self, node):
    if node in self.visited:
      return
    self.visited.add(node)
    
    for next_node in self.graph[node]:
      self.visit(next_node)
  
  def search(self, start_node):
    self.visited = set()
    self.visit(start_node)
    return self.visited

d = DFS([1,2,3,4,5])

d.add_edge(1,2)
d.add_edge(1,3)
d.add_edge(1,4)
d.add_edge(2,4)
d.add_edge(2,5)
d.add_edge(3,4)
d.add_edge(4,5)

print(d.search(1))
# this means that all nodes in the graph are reachable from 1
print("--------------------------------------------------")

# Components and connectivity
# a component of a graph contains nodes that are reachable from  each other using the edges of the graph.
# the following has 3 components: {1,2,3}, {4,5,6,7}. {8}
graph2 = "graph2.png"

# the graph is connected if it has exactly one component, i.e, if there is a path between any two nodes. 
# the follwoing graph is connected since its only component is {1,2,3,4,5}
graph = "graph.png"

# using the DFS we can compute components of a graph by iterating through all nodes and starting a new 
# seach whenever we encounter a node that is not yet in any component.
class Components:
  def __init__(self, nodes):
    self.nodes = nodes
    self.graph = {node: [] for node in nodes}
  
  def add_edge(self, a, b):
    self.graph[a].append(b)
    self.graph[b].append(a)
  
  def visit(self, node):
    if node in self.components:
      return
    self.components[node] = self.counter

    for next_node in self.graph[node]:
      self.visit(next_node)
    
  def find_components(self):
    self.counter = 0
    self.components = {}

    for node in self.nodes:
      if node not in self.components:
        self.counter += 1
        self.visit(node)
    
    return self.components
  
# counter: stores number of components. Whenever a node that does not belong to any of the existing 
# components is found, the variable is incremented by 1 (creating a new component)
# the new component is initially empty and is then filled using a depth-first search. The dictionary
# "components" stores the component of each node visited so far
# counter: used as the identifier of the component during the depth-first search

c = Components([1,2,3,4,5])

c.add_edge(1,2)
c.add_edge(3,4)
c.add_edge(3,5)
c.add_edge(4,5)

print(c.find_components())
print("--------------------------------------------------")
# this graph has 2 components: {1,2}, {3,4,5}

# Breadth-frist Search
# BFS is another technique for iterating through the nodes of a graph. similarly to DFS, BFS starts at a
# given node and visits all ndoes that are reachable from the start node using edges of the graph.
# the difference between the two techniqaues is the order in which the nodes are visited

# BFS is implemented as follows:
class BFS:
  def __init__(self, nodes):
    self.nodes = nodes
    self.graph = {node: [] for node in nodes}
  
  def add_edge(self, a, b):
    self.graph[a].append(b)
    self.graph[b].append(a)
  
  def search(self, start_node):
    visited = set()
    
    queue = [start_node]
    visited.add(start_node)

    for node in queue:
      for next_node in self.graph[node]:
        if next_node not in visited:
          queue.append(next_node)
          visited.add(next_node)
    
    return visited
  
# queue: contains the nodes to be processed. Initially, list contains the start node. In each step of
# the main loop, the seatch takes the next node from the queue and goes through the adjacency list of
# the node. Any node on the adjacency list that has not been visited yet is added to the queue

b = BFS([1,2,3,4,5])

b.add_edge(1,2)
b.add_edge(1,3)
b.add_edge(1,4)
b.add_edge(2,4)
b.add_edge(2,5)
b.add_edge(3,4)
b.add_edge(4,5)

print(b.search(1))
print("--------------------------------------------------")

# Shortest paths and distances
# the shortest path between two nodes in a graph is a path connecting two nodes with the < amount of edges
# the distance of two nodes is the length of the shortest path between them

# the shortest path from the node 1 -> 5 is: 1 -> 2 -> 5 (2)
graph = "graph.png"

class Distances:
  def __init__(self, nodes):
    self.nodes = nodes
    self.graph = {node: [] for node in nodes}
  
  def add_edge(self, a, b):
    self.graph[a].append(b)
    self.graph[b].append(a)

  def find_distances(self, start_node):
    distances = {}

    queue = [start_node]
    distances[start_node] = 0

    for node in queue:
      distance = distances[node]
      for next_node in self.graph[node]:
        if next_node not in distances:
          queue.append(next_node)
          distances[next_node] = distance + 1

    return distances

# same as previous code, but now the set visited has been replaced by the disctionary distances that
# stores the discovered distances

d = Distances([1,2,3,4,5])

d.add_edge(1,2)
d.add_edge(1,3)
d.add_edge(1,4)
d.add_edge(2,4)
d.add_edge(2,5)
d.add_edge(3,4)
d.add_edge(4,5)

print(d.find_distances(1)) # {1: 0, 2: 1, 3: 1, 4: 1, 5: 2}
# distance tonode 1 is 0
# distance tonode 2 is 1
# distance tonode 3 is 1
# distance tonode 4 is 1
# distance tonode 5 is 2
print("--------------------------------------------------")

# using BFS we can implement a class that finds the shortest path between two nodes
class ShortestPaths:
  def __init__(self, nodes):
    self.nodes = nodes
    self.graph = {node: [] for node in nodes}
  
  def add_edge(self, a, b):
    self.graph[a].append(b)
    self.graph[b].append(a)

  def find_path(self, start_node, end_node):
    distances = {}
    previous = {}

    queue = [start_node]
    distances[start_node] = 0
    previous[start_node] = None

    for node in queue:
      distance = distances[node]
      for next_node in self.graph[node]:
        if next_node not in distances:
          queue.append(next_node)
          distances[next_node] = distance + 1
          previous[next_node] = node
      
    if end_node not in distances:
      return None
    
    node = end_node
    path = []
    while node:
      path.append(node)
      node = previous[node]
    
    path.reverse()
    return path
# find_path: gets nodes start_node and end_node as parameters and finds the shortest path between them
# dict distances: stores distances to the start noda as before.
# dict previous: stores for each node the preceding node on the shortest path.
# using the dict previous we can trace back the shortest path from the end node back to the start node
# the path is then reversed before returning
s = ShortestPaths([1,2,3,4,5])

s.add_edge(1,2)
s.add_edge(1,3)
s.add_edge(1,4)
s.add_edge(2,4)
s.add_edge(2,5)
s.add_edge(3,4)
s.add_edge(4,5)

print(s.find_path(2,4))
print(s.find_path(1,5))
print(s.find_path(5,1))
print("--------------------------------------------------")

# Labirinth as a Graph
# consider the following labyrinth, where the white squares are floor and the black squares are wall
labyrinth = "labyrinth.png"

# we can use DFS or BFS to find routes. We can use graph nodes to represent the floor squares and edges
# we could build a graph based on the description of the labyrinth, and we can use the labyrinth itself
# as a graph

def explore(grid, y, x):
  if grid[y][x] != 0:
    return
  
  print("visit", y, x)
  grid[y][x] = 2

  explore(grid, y-1, x)
  explore(grid, y+1, x)
  explore(grid, y, x-1)
  explore(grid, y, x+1)

grid = [[1,1,1,1,1,1,1,1],
        [1,0,0,0,0,0,0,1],
        [1,0,1,0,1,1,0,1],
        [1,0,1,1,0,0,0,1],
        [1,0,0,0,0,1,0,1],
        [1,1,1,1,1,1,1,1]]

explore(grid, 1, 1)

for row in grid:
  print(row)
print("--------------------------------------------------")
# lab is  given a 2 dimensional list: 0(floor), 1(wall). the function explore performs DFS in the lab
# so that the visited squares are marked with the value 2

# explore: 2 coordinates of a square and it first checks the number in the square. If the number is not 0,
# the function exits, because then the square is either a wall(1) or a floor that has been visited already(2)
# then the function contionues with recursive calls for the adjacent squares above, below, left and right
