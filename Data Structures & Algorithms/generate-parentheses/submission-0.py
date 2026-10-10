class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans, sol = [], []
        def dfs(stack):
            if len(sol) > 2*n: return
            if len(sol) == 2*n and stack == []:
                ans.append("".join(sol[:]))
                return
            
            for p in [")", "("]:
                if stack and stack[-1] == '(' and p == ')':
                    sol.append(p)
                    dfs(stack[:-1])
                    sol.pop()
                elif p == '(':
                    sol.append(p)
                    dfs(stack[:] + [p])
                    sol.pop()
                else:
                    continue
                
            return
        dfs([])
        return ans