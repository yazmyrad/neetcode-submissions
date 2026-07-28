class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        hashset = defaultdict(int)
        for n in nums:
            if n in hashset: continue
            hashset[n] = 1
            if n-1 in hashset:
                hashset[n] = hashset[n-1]+1
            k = n+1
            while k in hashset:
                hashset[k] = hashset[k-1]+1
                k += 1
        return max(hashset.values())