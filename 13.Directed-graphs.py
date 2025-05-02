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
# dynamic programming can be used for computing with directed acyclic graphs. the following can be 
# answered using dynamic programming
  # how many different paths are there from a node "a" to a node "b"
  # what is the smallest number of edges on a path from a node "a" to a node "b"
  # what is the largest number of edges on a path from a node "a" to a node "b"

graph3 = "graph03.png"
# there are 3 different paths from node 4 to node 3
  # 4 -> 1 -> 2 -> 3
  # 4 -> 5 -> 2 -> 3
  # 4 -> 5 -> 3
# when counting paths from the node 4 to node 3, we can divide the problem into two subproblems
  # first edge of the path is 4 -> 1: count the paths from node 1 to node 3
  # first edge of the path is 4 -> 5: count the paths from node 5 to node 3
# more generaly , when counting paths from a node x to y, we iterate through all nodes that are reachahble 
# by an edge from the node x. summing up all paths from such nodes to the node y gives the number of paths
# from node x to node y

# when graph is acyclic, all subproblems can be computed efficiently using dynamic programming
class CountPaths:
  def __init__(self, nodes):
    self.nodes = nodes
    self.graph = {node: [] for node in self.nodes}
  
  def add_edge(self, a, b):
    self.graph[a].append(b)
  
  def count_from(self, node):
    if node in self.result:
      return self.result[node]
    
    path_count = 0
    for next_node in self.graph[node]:
      path_count += self.count_from(next_node)

    self.result[node] = path_count
    return path_count
  
  def count_paths(self, x, y):
    self.result = {y: 1}
    return self.count_from(x)

# alg usage
c = CountPaths([1, 2, 3, 4, 5, 6])

c.add_edge(1, 2)
c.add_edge(2, 3)
c.add_edge(3, 6)
c.add_edge(4, 1)
c.add_edge(4, 5)
c.add_edge(5, 2)
c.add_edge(5, 3)

print(c.count_paths(4, 3)) # 3
print("--------------------------------------------------")
# here, dynamic programic is realized by storing path counts from each node to the target node into 
# a dictionary result. If the path count is alreadyh stored, it is not computed again, which makes
# the alg efficient

# Problems as graphs
# consider the exercise that was solved in dynamic programming ch.10
# you have unlimited number of coins with values given as a list. how many ways can you chose the coins
# so that their sum is x.
# [1,3,4], x=6, answer=9 ways

# the problem can be represented as a graph, where each node represents one of the sums 0,1,...,x and
# there is an edge from node a to node b if adding one coin to the sum a gives the sum b.
# the graph looks like this:
graph5 = "graph05.png"
# each path from node 0 to x represents one way of obtaining the sum x.

# Strong connectivity
# in directed graphs, the concept of connectivity is more complicated than in undirected graphs, because
# two nodes are not necessarily connected by a directed path even if they are in the same component.

# consider the following
graph6 = "graph06.png"
# in the left graph, there is a path from any node to any other node
# in the right graph, there is no path from node 2 to node 1

graph6 = "graph06.png"
# directed grapths are strongly connected, if there is as directed path from any node to any other node.
  # graph on the left is strongly connected
  # graph on the right isn't strongly connected

# the strongly connected componenets of  a directed graph are mixamal sets of nodes such that there is
# a path from any node in the set to any other node in the set. 
# graphs can be partitioned into strongly connected components.

# [1,2], [3,6,7] are strongly connected,  
graph7 = "graph07.png"

# the figure shows the strongly connected components as a graph, where each node corresponds to 1 component
graph8 = "graph08.png"
# here the components are: A={1,2}, B={3,6,7}, C={4}, D={5}

# Kosaraju's alg
# the strongly connected componenets of a graph can be computed using Kosaraju's algorithm.
# it has 2 phases -> eahc of which visits all nodes using DFS

# Fase 1: constructs a list of all nodes in the same way as in topological sorting (not checking for cycles)
# Fase 2: perfromed in the transpose graph, where the direction of every edge as been reversed. the alg
# iterates through the node list constructed in fase1 in reverse order, and starts a DFS for each node that
# hasn't been visited. for each DFS, the nodes visited during the seach from a strongly connected component

class Kosaraju:
  def __init__(self, nodes):
    self.nodes = nodes
    self.graph = {node: [] for node in self.nodes}
    self.reverse = {node: [] for node in self.nodes}
  
  def add_edge(self, a, b):
    self.graph[a].append(b)
    self.reverse[b].append(a)
  
  def visit(self, node, phase):
    if node in self.visited:
      return
    self.visited.add(node)

    if phase == 1:
      graph = self.graph
    if phase == 2:
      graph = self.reverse
    
    for next_node in graph[node]:
      self.visit(next_node, phase)
    
    if phase == 1:
      self.order.append(node)
  
  def count_components(self):
    self.visited = set()
    self.order = []

    for node in self.nodes:
      self.visit(node, 1)
    
    self.order.reverse()
    self.visited.clear()

    count = 0
    for node in self.order:
      if node not in self.visited:
        count += 1
        self.visit(node, 2)
    
    return count

# implementation  
k = Kosaraju([1, 2, 3, 4, 5, 6, 7])
k.add_edge(1, 2)
k.add_edge(1, 4)
k.add_edge(2, 1)
k.add_edge(2, 5)
k.add_edge(3, 2)
k.add_edge(3, 7)
k.add_edge(5, 4)
k.add_edge(6, 3)
k.add_edge(6, 5)
k.add_edge(7, 6)
print(k.count_components())
print("--------------------------------------------------")