class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans, sol = [], []
        def dfs(i):
            if sum(sol) > target: return
            if sum(sol) == target:
                ans.append(sol[:])
                return
            
            for j in range(i, len(nums)):
                sol.append(nums[j])
                dfs(j)
                sol.pop()
            return
        dfs(0)
        return ans