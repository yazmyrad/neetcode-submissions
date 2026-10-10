class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans, sol = [], []
        def dfs(op, cl):
            if len(sol) > 2*n: return
            if len(sol) == 2*n:
                ans.append("".join(sol[:]))
                return
            
            for p in ["(", ")"]:
                if p == ')' and cl < op:
                    sol.append(p)
                    dfs(op, cl+1)
                    sol.pop()
                elif p == '(' and op < n:
                    sol.append(p)
                    dfs(op+1, cl)
                    sol.pop()
                else:
                    continue
                
            return
        dfs(0, 0)
        return ans