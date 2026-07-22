class Solution:
    def makefreq(self, word: str)->Dict:
        hashmap = {}
        for s in word:
            if s in hashmap:
                hashmap[s]+=1
            else:
                hashmap[s]=0

        return hashmap

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freqs = []
        for word in strs:
            freqs.append(self.makefreq(word))
        checked = [0]*len(strs)
        j = 0
        answ = []
        while j<len(strs):
            if checked[j]: 
                j+=1
                continue
            group = [strs[j]]
            j+=1
            for i in range(j, len(strs)):
                print()
                if freqs[i] == freqs[j-1] and not checked[i]:
                    group.append(strs[i])
                    checked[i] = 1
                
            answ.append(group)
        return answ