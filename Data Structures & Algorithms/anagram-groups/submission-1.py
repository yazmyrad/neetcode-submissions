class Solution:
    def makefreq(self, word: str)->Dict:
        hashmap = [0]*26
        for s in word:
            hashmap[ord(s)-ord('a')] += 1
        return hashmap

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freqs = defaultdict(list)
        for word in strs:
            freq = self.makefreq(word)
            freqs[tuple(freq)].append(word)

        return list(freqs.values())