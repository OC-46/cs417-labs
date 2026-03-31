"""
Lab 16: Graphs — BFS and DFS

Graph class (complete — read and use it) and traversal functions (your job).
"""

from collections import deque


# ── Graph Class (provided) ─────────────────────────────────────────

class Graph:
    """An undirected graph using an adjacency list."""

    def __init__(self):
        self._adj = {}  # {label: [neighbor, ...]}

    def add_node(self, label):
        """Add a node to the graph. Does nothing if it already exists."""
        if label not in self._adj:
            self._adj[label] = []

    def add_edge(self, a, b):
        """Add an undirected edge between nodes a and b.

        Creates the nodes if they don't exist yet.
        """
        self.add_node(a)
        self.add_node(b)
        if b not in self._adj[a]:
            self._adj[a].append(b)
        if a not in self._adj[b]:
            self._adj[b].append(a)

    def get_neighbors(self, label):
        """Return the list of neighbors for the given node.

        Returns an empty list if the node doesn't exist.
        """
        return self._adj.get(label, [])

    def has_node(self, label):
        """Return True if the node exists in the graph."""
        return label in self._adj

    def nodes(self):
        """Return a list of all node labels."""
        return list(self._adj.keys())

    def __repr__(self):
        return f"Graph({dict(self._adj)})"


# ── Task 1: Build the Graph ───────────────────────────────────────

def build_lab_graph():
    """Build and return the lab graph.

    The graph looks like this:

        A
       / \\
      B   C
      |   |
      D   E
       \\ /
        F

    Edges: A-B, A-C, B-D, C-E, D-F, E-F
    """
    g = Graph()
    add_edge = g.add_edge
    for node in "ABCDEF":
        g.add_node(node)

    # Add all six edges
    add_edge("A", "B")
    add_edge("A", "C")
    add_edge("B", "D")
    add_edge("C", "E")
    add_edge("D", "F")
    add_edge("E", "F")

    return g


# ── Task 2: Breadth-First Search ──────────────────────────────────

def bfs(graph, start):
    """Traverse the graph in breadth-first order starting from `start`.

    Returns a list of node labels in the order they were visited.
    """
    visited = set()
    order = []
    frontier = deque()
    start = start
    frontier.append(start)
    visited.add(start)


    while frontier:
        current = frontier.popleft()
        order.append(current)

        for neighbor in graph.get_neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                frontier.append(neighbor)

    return order


# ── Task 3: Depth-First Search ────────────────────────────────────

def dfs(graph, start):
    """Traverse the graph in depth-first order starting from `start`.

    Returns a list of node labels in the order they were visited.
    Uses an iterative approach with a stack (not recursion).
    """
    visited = set()
    order = []
    stack = []

    start = start
    stack.append(start)
    visited.add(start)

    while stack:
        current = stack.pop()
        order.append(current)

        if current not in visited:
            continue
        else:            
            visited.add(current)
        
        for neighbor in graph.get_neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)

    return order


# ── Task 4: Find Path ────────────────────────────────────────────

def find_path(graph, start, goal):
    """Find the shortest path from `start` to `goal` using BFS.

    Returns a list of node labels representing the path (including both
    start and goal). Returns an empty list if no path exists.
    """
    if start == goal:
        return [start]

    visited = set()
    frontier = deque()
    parent = {}
    start = start
    frontier.append(start)
    visited.add(start)

    while frontier:
        current = frontier.popleft()
        if current == goal:
            path = []
            while current != start:
                path.append(current)
                current = parent[current]
            path.append(start)
            return list(reversed(path))

        for neighbor in graph.get_neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                frontier.append(neighbor)

    return []  # No path found
