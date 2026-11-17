class Graph:

    def __init__(self, n: int, edges: list[list[int]]):
        self.adj = [[float('inf')] * n for _ in range(n)]

        for i in range(n):
            self.adj[i][i] = 0

        for u, v, w in edges:
            self.adj[u][v] = min(self.adj[u][v], w)

        # Floyd-Warshall initialization
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    self.adj[i][j] = min(
                        self.adj[i][j],
                        self.adj[i][k] + self.adj[k][j]
                    )

    def addEdge(self, edge: list[int]) -> None:
        u, v, w = edge
        n = len(self.adj)

        for i in range(n):
            for j in range(n):
                self.adj[i][j] = min(
                    self.adj[i][j],
                    self.adj[i][u] + w + self.adj[v][j]
                )

    def shortestPath(self, node1: int, node2: int) -> int:
        ans = self.adj[node1][node2]
        return ans if ans != float('inf') else -1