class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        chars = [0]*26
        for c in s:
            chars[ord(c)-ord('a')] += 1
        for c in t:
            if chars[ord(c)-ord('a')] == 0: return False
            chars[ord(c)-ord('a')] -= 1
        return True