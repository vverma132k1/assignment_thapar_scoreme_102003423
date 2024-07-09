### 2. `main.py`

# python
"""
Assignment: Implement the most efficient algorithm to solve the given problem.

Problem Statement:
You are given a Directed Acyclic Graph (DAG) with `n` nodes, numbered from `0` to `n-1`.
The graph is represented as an adjacency list where `graph[i]` is a list of tuples `(j, w)`,
representing an edge from node `i` to node `j` with weight `w`. Your task is to find the longest
path in the graph starting from any node.

Function Signature:
def longest_path(graph: list) -> int:

Parameters:
- graph (list): A list of lists, where `graph[i]` contains tuples `(j, w)` representing an edge
  from node `i` to node `j` with weight `w`.

Returns:
- int: The length of the longest path in the graph.

Example:
>>> graph = [
...     [(1, 3), (2, 2)],
...     [(3, 4)],
...     [(3, 1)],
...     []
... ]
>>> longest_path(graph)
7
"""

def longest_path(graph: list) -> int:
    """
    Find the longest path in a DAG.
    """
    topo_order = topological_sort(graph)
    return calculate_longest_path(graph, topo_order)

def topological_sort(graph):
    """
    Perform a topological sort of the graph.
    """
    def dfs(node):
        visited[node] = True
        for neighbor, weight in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor)
        topo_order.append(node)
    
    n = len(graph)
    visited = [False] * n
    topo_order = []
    
    for i in range(n):
        if not visited[i]:
            dfs(i)
    
    return topo_order[::-1]

def calculate_longest_path(graph, topo_order):
  """
  Calculate the longest path using the topological order.
  """
  n = len(graph)
  distances = [0] * n  # Initialize all distances to 0

  for node in topo_order:
    for neighbor, weight in graph[node]:
      # Update neighbor distance considering existing distance
      distances[neighbor] = max(distances[neighbor], distances[node] + weight)

  return max(distances)
