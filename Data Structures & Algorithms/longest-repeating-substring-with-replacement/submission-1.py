class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 1:
            return 1
        hashtable = defaultdict(int)
        i = 0
        maxlen = 1
        for j in range(len(s)):
            hashtable[s[j]] += 1
            while len(hashtable.keys()) > 1 and sum(hashtable.values()) - max(hashtable.values()) > k:
                hashtable[s[i]] -= 1
                i += 1
            maxlen = max(maxlen, sum(hashtable.values()))
        return maxlen

                