# 16. Maximum flow

# a maximum flow graph is a flow wiht the largest possible total flow leaving the source. example of
# a maximum flow from the node 1 to node 5
max_flow01 = "max-flow-01.png"
# x/c means c is the edge capacy, of which, x is used by the flow.
  # 1-2 has capacity 4, all of which in use
  # 1-3 has capacity 6, of which 3 is the flow

# graph has max flow of 7, both outgoing of the node 1 and the incoming flow of node 5.

# Ford-Fulkerson Algorithm
# this alg modifies the graph byadding edges so that every edge has a reverse edge that connects the same
# pair of nodes in the opposite direction.
  # initially, these new edges all have capacity of 0
max_flow02 = "max-flow-02.png"

# the alg starts with a 0 flow and then increases the flow in stages. each stage, the alg chooses a path 
# from the source to the sink node, called augmenting path, and increases the flow along the path

# every edge on the augmenting path must have a positive cap.
# the flow along the path will be increased by x(smallest capacity of an edge on the path)
# then, for each edge on the path, the alg reduces the capacity of the edge by x and increases the cap of 
# the reverse edge by x.
# modeified capacities are called residual capacities and represent the capacity available to later
# augmenting paths

# alg keeps increaseing the flow by finding augmenting paths until no path with positive residual caps can
# be found. final flow constructed by the alg is a maximum flow
max_flow03 = "max-flow-03.png"

# implementation
class MaximumFlow:
  def __init__(self, nodes):
    self.nodes = nodes
    self.graph = {}
    for i in self.nodes:
      for j in self.nodes:
        self.graph[(i,j)] = 0
  
  def add_edge(self, node_a, node_b, capacity):
    self.graph[(node_a, node_b)] += capacity

  def add_flow(self, node, sink, flow):
    if node in self.seen:
      return 0
    self.seen.add(node)
    if node == sink:
      return flow
    for next_node in self.nodes:
      if self.flow[(node, next_node)] > 0:
        new_flow = min(flow, self.flow[(node, next_node)])
        inc = self.add_flow(next_node, sink, new_flow)
        if inc > 0:
          self.flow[(node, next_node)] -= inc
          self.flow[(next_node, node)] += inc
          return inc
    
    return 0
  
  def construct(self, source, sink):
    self.flow = self.graph.copy()
    total = 0
    while True:
      self.seen = set()
      add = self.add_flow(source, sink, float("inf"))
      if add  == 0:
        break
      total += add
    return total
  
# implementation
m = MaximumFlow([1, 2, 3, 4, 5])
m.add_edge(1, 2, 4)
m.add_edge(1, 3, 6)
m.add_edge(2, 3, 8)
m.add_edge(2, 4, 3)
m.add_edge(3, 5, 4)
m.add_edge(4, 5, 5)
print(m.construct(1, 5)) # 7
