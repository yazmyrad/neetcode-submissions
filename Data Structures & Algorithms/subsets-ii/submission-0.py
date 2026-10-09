class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans, sol = [], []
        def dfs(i:int):
            ans.append(sol[:])
            
            for j in range(i, len(nums)):
                if j>i and nums[j] == nums[j-1]: continue

                sol.append(nums[j])

                dfs(j+1)
                sol.pop()
            return
        nums.sort()
        dfs(0)
        return ans