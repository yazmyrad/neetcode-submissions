class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans, sol = [], [None]*len(nums)
        def dfs(idx: int):
            if idx == len(nums): 
                ans.append(sol[:])
                return
            for i in range(len(nums)):
                if nums[i] in sol: continue

                sol[idx] = nums[i]
                dfs(idx+1)
                sol[idx] = None
            return
        dfs(0)
        return ans
