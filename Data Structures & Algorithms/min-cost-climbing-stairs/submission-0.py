class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n == 2:
            return min(cost)
        ans = [0]*(n+1)
        for i in range(2, n+1):
            ans[i] = min(ans[i-1]+cost[i-1], ans[i-2]+cost[i-2])
        #print(ans)
        return ans[-1]