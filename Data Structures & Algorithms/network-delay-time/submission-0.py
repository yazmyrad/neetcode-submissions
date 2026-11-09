class Solution:
    def shortest_path(self, graph: List[List[Tuple[int, int]]], start, target, n):
        dist = [float("inf")] * n
        dist[start-1] = 0
        hp = [(0, start)]              
        visited = set()
        while hp:
            d, node = heapq.heappop(hp)
            if node in visited:
                continue
            if node == target:
                return d
            visited.add(node)
            for neigh, w in graph[node]:
                nd = d + w
                if nd < dist[neigh-1]:
                    dist[neigh-1] = nd
                    heapq.heappush(hp, (nd, neigh))

        return -1   

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i: [] for i in range(1, n + 1)}

        for u, v, w in times:
            adj[u].append((v, w))

        time = []
        for target in range(1, n+1):
            delay = self.shortest_path(adj, k, target, n)
            if delay == -1: return -1
            time.append(delay)
        return max(time)