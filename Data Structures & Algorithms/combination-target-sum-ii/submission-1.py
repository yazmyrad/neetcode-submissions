class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans, sol = [], []
        def dfs(i, sm):
            if sm == target:
                ans.append(sol[:])
                return
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                if sm + candidates[j] > target: continue
                sm += candidates[j]
                sol.append(candidates[j])
                dfs(j+1, sm)
                sm -= candidates[j]
                sol.pop()
            return
        candidates.sort()
        dfs(0, 0)
        return ans