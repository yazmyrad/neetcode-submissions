class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for i, point in enumerate(points):
            x, y = point
            distance = (x*x+y*y)
            heapq.heappush(distances, (distance, i))
        ans = []
        for _ in range(k):
            _, point = heapq.heappop(distances)
            ans.append(points[point])
        return ans