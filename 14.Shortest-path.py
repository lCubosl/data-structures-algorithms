# 14. Shortest-path

# the follwoing graph shows the example of a weighted graph
shortest_path= "shortest-path.png"
# each edge is labeled with it's weight.
  # 1->3->2 is 1+4=5 
    # 1->3 has weight 1 and 
    # 3->2 has weight 4

# earlier we used BFS to find shortest paths, but it doesn't work correctly in weighted graphs.
# lets see some algorithms to help traverse weighted paths

# Bellman-ford algroithm
# computes distance grom given start node to all nodes. mantains an estimate for the distance to each node
# initially, distance of the start node is 0 and distance to all other nodes is INFINITY

# alg performs n-1 rounds of computation, wehere n is the number of nodes in the graph
  # each round, alg iterates through all edges of graph and tries to use each edge  to reduce 
  # distance estimate
  # when algorithm is processing a->b, it checks if the distance to b trhough this edge is smaller than
  # the previous  esitmate.
  # if it is, the  distance to b is updates

# after n-1 rounds, all distances have reached their final valus and correspond to the lengths of 
# the shortest paths

class BellmanFord:
  def __init__(self, nodes):
    self.nodes = nodes
    self.edges = []

  def add_edge(self, node_a, node_b, weight):
    self.edges.append((node_a, node_b, weight))
  
  def find_distances(self, start_node):
    distances = {}
    for node in self.nodes:
      distances[node] = float("inf")
    distances[start_node] = 0

    num_rounds = len(self.nodes) - 1
    for _ in range(num_rounds):
      for edge in self.edges:
        node_a, node_b, weight = edge
        new_distance = distances[node_a] + weight

        if new_distance < distances[node_b]:
          print("update", node_a, node_b, new_distance)
          distances[node_b] = new_distance
    
    return distances

# implementation
b = BellmanFord([1, 2, 3, 4, 5])
b.add_edge(1, 2, 8)
b.add_edge(1, 3, 1)
b.add_edge(2, 5, 5)
b.add_edge(3, 2, 4)
b.add_edge(3, 4, 2)
b.add_edge(4, 2, 1)
b.add_edge(4, 5, 3)
distances = b.find_distances(1)
print(distances)
print("--------------------------------------------------")

# distances, and the corresponding shortest paths:
# t_node | distance | path
# 1      | 0        | 1
# 2      | 4        | 1-3-4-2
# 3      | 1        | 1-3
# 4      | 3        | 1-3-4
# 5      | 6        | 1-3-4-5

# example first update node 1-2 is updated to distance 8 because its shorter than infinity
# the distance to a node can change multiple times
  # distance to node 2 is first 8
  # through edge 3-2 is updated to 5 (5 < 8)
  # through edge 4-2 is then updated to 4 (4 < 5)

# after k rounds, the algorithm has found all shortest paths consisting of at most k edges
# in a graph with n nodes, every shortest path has at most n - 1edges. if a path n as more edges, it
# visits some nodes multiple times (cannot be the shortest path)
# bellman-ford algorithm needs at most n-1 rounds to find all shortest paths

# alg performs n-1 rounds and each round processes m edges. time complexity of O(n * m)

# Negative cycles
# if the graph has a negative cycle, the bellman-ford alg does not produce a sensible result.
b = BellmanFord([1, 2, 3, 4])

b.add_edge(1, 2, 1)
b.add_edge(2, 3, 1)
b.add_edge(3, 2, -2)
b.add_edge(2, 4, 1)

distances = b.find_distances(1)
print(distances) # {1: 0, 2: -2, 3: 0, 4: -1}
print("--------------------------------------------------")
# in this example, each round reduces the length of the path by 1. the length can be made arbitrarily small
# and the distances meaningless

# Bellman-ford algorithm can be used for detecting a negative cycle by performing one more round after n-1.
# if the graph has a negative cycle, that is reachable from the start node, some distances still change
# in the extra round, which can be detected by the algorithm

# Dijkstra's Algorithm
# similar to Bellman-ford alg. beggining is the same. node 0 is the start node and INFINITY for all others
# also cannot be used if the graph has negative edge weights
# each step, the algorithm selects the node with the smallest distance among nodes that have not been 
# selected before. at this point, the distance to selected node has reached its final value and does not
# cahnge any more.
# alg goes through edges leaves the node and uses them to reduce distances of other nodes.
# then the node is marked as visited and will not be processed again

import heapq

class Dijkstra:
  def __init__(self, nodes):
    self.nodes = nodes
    self.graph = {node: [] for node in nodes}

  def add_edge(self, node_a, node_b, weight):
    self.graph[node_a].append((node_b, weight))
  
  def find_distances(self, start_node):
    distances = {}
    for node in self.nodes:
      distances[node] = float("inf")
    distances[start_node] = 0

    queue = []
    heapq.heappush(queue, (0, start_node))

    visited = set()
    while queue:
      node_a = heapq.heappop(queue)[1]
      if node_a in visited:
        continue
      visited.add(node_a)

      for node_b, weight in self.graph[node_a]:
        new_distance = distances[node_a] + weight
        
        if new_distance < distances[node_b]:
          distances[node_b] = new_distance
          new_pair = (new_distance, node_b)
          heapq.heappush(queue, new_pair)
    
    return distances

# implementation
d = Dijkstra([1, 2, 3, 4, 5])

d.add_edge(1, 2, 8)
d.add_edge(1, 3, 1)
d.add_edge(2, 5, 5)
d.add_edge(3, 2, 4)
d.add_edge(3, 4, 2)
d.add_edge(4, 2, 1)
d.add_edge(4, 5, 3)

distances = d.find_distances(1)
print(distances) # {1: 0, 2: 4, 3: 1, 4: 3, 5: 6}
print("--------------------------------------------------")

# in each step, dijkstra's alg sleects the node with the smallest distance. the distance to the selected
# node should not change since it will not be selected again

# the alg reliest on the assumption that there are no negative edge weights. When  a node with the smallest
# distance is selected, all the remaining distances on the heap are greater or equal, therefore, no later
# distance update can produce a smaller distance, and the distance to the selected node will not change

# time complexity O(n + m logm)
  # O(n): iterating through nodes
  # O(m logm): at most, one element is added to the heap for each edge.
    # O(m): heap operations
    # O(logm): each heap operation needs O(logm) time

# Dijkstra's alg can produce incorrect results if the graph has negative edges
d = Dijkstra([1, 2, 3, 4])

d.add_edge(1, 2, 3)
d.add_edge(2, 3, -4)
d.add_edge(1, 3, 1)
d.add_edge(3, 4, 1)

distances = d.find_distances(1)
print(distances) # [0, 3, -1, 2]
print("--------------------------------------------------")

# shortest path 1 to 4 should have length 0 (1-2-3-4 w/ length 3-4+1=0)
# the alg selects node 3, with distance 1, which updates the distance to node 4 to 2. later, the distance
# to 3 is updated to -1, due to the negative edge, but since the node has already been marked as visited,
# its not processed again and the distance to 4 doesnt get updated

# Constructing shortest paths
# Besides the 2 algs already studied, we can construct a shortest path from a start to an end node, by
# augmenting each distance with the edge that caused the update to its current value. then, we can
# compute the path to each node by walking the path backwards

# Bellman-Ford alg returning shortest path instead of distances
class BellmanFordSP:
  def __init__(self, nodes):
    self.nodes = nodes
    self.edges = []

  def add_edge(self, node_a, node_b, weight):
    self.edges.append((node_a, node_b, weight))

  def shortest_path(self, start_node, end_node):
    distances = {}
    for node in self.nodes:
      distances[node] = float("inf")
    distances[start_node] = 0
    previous = {}
    previous[start_node] = None

    for _ in range(len(self.nodes) - 1):
      for edge in self.edges:
        node_a, node_b, weight = edge
        new_distance = distances[node_a] + weight
        if new_distance < distances[node_b]:
          distances[node_b] = new_distance
          previous[node_b] = node_a
    
    if distances[end_node] == float("inf"):
      return None
    
    path = []
    node = end_node
    while node:
      path.append(node)
      node = previous[node]

    path.reverse()
    return path
  
b = BellmanFordSP([1, 2, 3, 4, 5])

b.add_edge(1, 2, 8)
b.add_edge(1, 3, 1)
b.add_edge(2, 5, 5)
b.add_edge(3, 2, 4)
b.add_edge(3, 4, 2)
b.add_edge(4, 2, 1)
b.add_edge(4, 5, 3)

path = b.shortest_path(1, 5)
print(path) # [1, 3, 4, 5]
print("--------------------------------------------------")

# Floyd-Warshall algorithm
# finds the distances between all pairs of ndoes at the same time rather than just the distances from 
# a single start node. works for any graph as long as there are no negative cycles

# represents the graph using an adjacency matrix, where the element on row a and colmn b stores the weight 
# of the edge from the node a to the node b. If a=b, the weight is 0, if there is no edge from the  node a
# to the node b, the weight is INFINITY
shortest_path= "shortest-path.png"

# the graph can be represented as the following adjacency matrix (" = INFINITY)
#   | 1 | 2 | 3 | 4 | 5
# 1 | 0 | 8 | 1 | " | "
# 2 | " | 0 | " | " | 5
# 3 | " | 4 | 0 | 2 | "
# 4 | " | 1 | " | 0 | 3
# 5 | " | " | " | " | 0

# main part of the algorithms consists of three nested loops.
  # first loop: chooses a middle node k
  # second and third: choose a start node and a end node
# then, the alg checks if the distance from the start node to end node can be shortened using a path
# that goes through the midle node
class FloydWarshall:
  def __init__(self, nodes):
    self.nodes = nodes
    self.graph = {}
    for a in self.nodes:
      for b in self.nodes:
        distance = 0 if a == b else float("inf")
        self.graph[(a,b)] = distance

  def add_edge(self, a, b, w):
    self.graph[(a,b)] = min(self.graph[(a,b)], w)
  
  def find_distances(self):
    distances = self.graph.copy()

    for k in self.nodes:
      for a in self.nodes:
        for b in self.nodes:
          distance = min(distances[(a,b)],
                         distances[(a,k)] + distances[(k,b)])
          distances[(a,b)] = distance
    
    return distances
  
# implementation
f = FloydWarshall([1, 2, 3, 4, 5])
f.add_edge(1, 2, 8)
f.add_edge(1, 3, 1)
f.add_edge(2, 5, 5)
f.add_edge(3, 2, 4)
f.add_edge(3, 4, 2)
f.add_edge(4, 2, 1)
f.add_edge(4, 5, 3)
distances = f.find_distances()
print(distances[(1, 4)]) # 3
print(distances[(2, 1)]) # inf
print(distances[(3, 5)]) # 5
print("--------------------------------------------------")
# for each three nodes k,a,b, the mehtod checks if going from a to k to b is shorter than going directly 
# from a to b using the current distances. If it is, the distance from a to b is updated

# Algorithm analysis
# the algorithm processes the node k (intermediate), and all othter intermediate nodes are in range
# 1,...., k-1. since k goes trhough all values 1,2,...,n, the distances at the end are the lengths of
# the shortest paths.

# since there are three nested loops, the alg is time complex of O(n^3)

# Utility
# Dijkstra's alg: good for finding shortest paths. is efficient. doesn not work with negative edges
# Bellman-Ford alg: works with negative edges but not negative cycles. alg is slow for large graphs
# Floyd-Warshall: distances are needed for ALL pairs of nodes