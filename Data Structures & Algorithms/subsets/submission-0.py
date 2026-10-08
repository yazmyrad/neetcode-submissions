class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = [len(nums)]
        sol = []
        def backtrack(i: int):
            if i == n[0]: 
                ans.append(sol[:])
                return 
            
            backtrack(i+1)
            
            sol.append(nums[i])    
            backtrack(i+1)
            sol.pop()
            return
            
        backtrack(0)
        return ans
