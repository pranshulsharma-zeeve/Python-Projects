from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(self, v, visited):
        visited[v] = True
        for i in self.graph[v]:
            if not visited[i]:
                self.dfs(i, visited)

    def is_connected(self):
        visited = {node: False for node in self.graph}
        # Find the first node and start DFS from there
        first_node = list(self.graph.keys())[0]
        self.dfs(first_node, visited)

        # Check if all nodes are visited
        for node in visited:
            if not visited[node]:
                return False
        return True

# Example usage:
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(3, 4)

if g.is_connected():
    print("The graph is connected.")
else:
    print("The graph is not connected.")
