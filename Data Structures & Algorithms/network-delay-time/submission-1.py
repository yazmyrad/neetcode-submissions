class Solution:
    def shortest_path(self, graph: List[List[Tuple[int, int]]], start, n):
        dist = [float("inf")] * n
        dist[start-1] = 0
        hp = [(0, start)]              
        visited = set()
        while hp:
            d, node = heapq.heappop(hp)
            if node in visited:
                continue
            visited.add(node)
            res = d
            for neigh, w in graph[node]:
                nd = d + w
                if nd < dist[neigh-1]:
                    dist[neigh-1] = nd
                    heapq.heappush(hp, (nd, neigh))

        return res if len(visited) == n else -1   

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i: [] for i in range(1, n + 1)}

        for u, v, w in times:
            adj[u].append((v, w))

        return self.shortest_path(adj, k, n)