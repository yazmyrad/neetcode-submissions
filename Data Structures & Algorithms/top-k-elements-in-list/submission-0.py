class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        for n in nums:
            hashmap[n] += 1
        freqs = [(-value, key) for key, value in hashmap.items()]
        heapq.heapify(freqs)
        answ = []
        for _ in range(k):
            answ.append(heapq.heappop((freqs))[1])
        return answ