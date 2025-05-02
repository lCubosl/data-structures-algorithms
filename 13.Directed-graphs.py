# 13. Directed Graphs

# earlier we assumed that the edges of a graph go both directions, i.e, that the graph is undirected.
# the following graph is undirected
graph1= "graph.png"

# we will now consider directed graphs, where the edges only go 1 direction, indicated by the arrows
graph2= "graph02.png"
# dealing with directed graphs is similar to undirected ones, but the edge directions change some things

# Representing directed graphs
# in programing, a directed graph can be represented using adjacency lists in the same way as an 
# undirected one, but each edge is added to only one adjacency list.
class Graph:
  def __init__(self, nodes):
    self.nodes = nodes
    self.graph = {node: [] for node in self.nodes}

  def add_edge(self, a, b):
    self.graph[a].append(b)

# since the graph is directed, the method add_edge adds the node b into the adjacency list on the node a,
# but it doesnt add de node a into the adjacency list of the node b.
# thus, the adjacency list contains only those nodes that can be reached by following an edge in the
# specified direction
g = Graph([1, 2, 3, 4, 5])

g.add_edge(1, 2)
g.add_edge(2, 4)
g.add_edge(2, 5)
g.add_edge(3, 1)
g.add_edge(4, 1)
g.add_edge(4, 5)
print("--------------------------------------------------")
# depth first search and breath-first seach work on directed graphs too. 

# Topological ordering
# topological ordering of a directed graph is an ordering of the nodes that satisfies the following
# condition:
  # is there is a derected path from node a to b, then the node a is before the node b in ordering
# consider:
graph3 = "graph03.png"
# one possible topological ordering for the graph is [4,1,5,2,3,6]
# the following figure displays the nodes in topological order, which makes all edges go from l to r
graph4 = "graph04.png"

# topological ordering exists only for acyclic graphs, which are graphs that contain no cycles. 
# A cycle is a path in the graph that returns back to the node it started from. A cycle makes
# topological ordering impossible because no node of the cycle can occur in the ordering before
# all other nodes of the cycle 

# Topological sorting
# can be computed using DFS. during the computation, each node is in one the three states
  # state 0: node hasnt been visited
  # state 1: node processing has started but has not dinished yet
  # state 2: node has been fully processed

# initially every node is state. the alg iterates through all nodes, and starts a dfs for each node that
# is still in state 0. when the search reaches a node, the state of dthe node changes to 1. when all edges 
# leaving the node have been processed, it becomes state 2

# the alg constructs a list. each node is added to the list at state 2. at the end, the list is reversed
# to obtain topological ordering.

# if the graph contains a cycle, its detected (enconters edge that leads to starting node in state 1)
class TopologicalSort:
  def __init__(self, nodes):
    self.nodes = nodes
    self.graph = {node: [] for  node in self.nodes}
  
  def  add_edge(self, a, b):
    self.graph[a].append(b)
  
  def visit(self, node):
    if self.state[node] == 1:
      self.cycle = True
      return
    if self.state[node] == 2:
      return
    
    self.state[node] = 1
    for next_node in self. graph[node]:
      self.visit(next_node)
    
    self.state[node] = 2
    self.order.append(node)

  def create(self):
    self.state = {}
    for node in self.nodes:
      self.state[node] = 0
    
    self.order = []
    self.cycle = False

    for node in self.nodes:
      if self.state[node] == 0:
        self.visit(node)

    if self.cycle:
      return None
    else:
      self.order.reverse()
      return self.order
    
t = TopologicalSort([1, 2, 3, 4, 5, 6])
t.add_edge(1, 2)
t.add_edge(2, 3)
t.add_edge(3, 6)
t.add_edge(4, 1)
t.add_edge(4, 5)
t.add_edge(5, 2)
t.add_edge(5, 3)
print(t.create())
print("--------------------------------------------------")

# Dynamic Programming
