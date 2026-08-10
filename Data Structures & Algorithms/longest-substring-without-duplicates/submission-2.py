class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not len(s): return 0
        if len(s) == 1: return 1

        i, j = 0, 1
        substring = {s[i]: 1}
        n = len(s)
        maxlen = 1
        while i < j and j < n:
            if s[j] in substring:
                while s[j] in substring:
                    del substring[s[i]]
                    i += 1
            substring[s[j]] = 1
            j += 1
            maxlen = max(maxlen, len(substring.keys()))
        
        return maxlen
