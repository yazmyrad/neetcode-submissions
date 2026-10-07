class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.hp = nums
        heapq.heapify_max(self.hp)
        self.k = k

    def add(self, val: int) -> int:
        heapq.heappush_max(self.hp, val)
        #print(heapq.nlargest(self.k, self.hp))
        return heapq.nlargest(self.k, self.hp)[-1]        
