class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        freq1 = [0]*26
        freq2 = [0]*26

        for i in range(len(s1)):
            freq1[ord(s1[i]) - ord('a')] += 1
            freq2[ord(s2[i]) - ord('a')] += 1
        
        matches = 0
        for i in range(26):
            matches += (1 if freq1[i] == freq2[i] else 0)
        
        j = len(s1)
        for i in range(len(s1), len(s2)):
            if matches == 26: return True

            freq2[ord(s2[i]) - ord('a')] += 1
            freq2[ord(s2[i-j]) - ord('a')] -= 1

            matches = 0
            for k in range(26):
                matches += (1 if freq1[k] == freq2[k] else 0)
                
        if matches == 26: return True
        return False