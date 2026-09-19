class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ans = []
        for i in range(len(tokens)):
            op = tokens[i]
            if op in ['+', '-', '*', '/']:
                oprd2 = ans.pop()
                oprd1 = ans.pop()
                match op:
                    case '-':
                        ans.append(oprd1 - oprd2)
                    case '+':
                        ans.append(oprd1 + oprd2)
                    case '*':
                        ans.append(oprd1 * oprd2)
                    case '/':
                        ans.append(int(oprd1 / oprd2))
            else:
                ans.append(int(op))
        return ans[-1]
