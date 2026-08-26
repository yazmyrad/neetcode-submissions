class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): return ""

        n = len(s)
        d = defaultdict(int)
        for char in t:
            d[char] += 1

        window = defaultdict(int)
        i, matches = 0, 0
        found = False
        ans = s
        for j in range(len(s)):          
            window[s[j]] += 1

            if s[j] in d and window[s[j]] == d[s[j]]:
                matches += 1

            while matches == len(d):
                ans = ans if len(ans) < j-i+1 else s[i:j+1]
                found = True
                window[s[i]] -= 1
                if s[i] in d and window[s[i]] < d[s[i]]: matches -= 1
                i += 1
                
        return ans if found else ""       