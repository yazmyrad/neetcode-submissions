class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = []
        for i, num in enumerate(nums):
            hashmap.append((num, i))
        hashmap = sorted(hashmap)
        i, j = 0, len(nums)-1
        while i<j:
            curr = hashmap[i][0]+hashmap[j][0] 
            if curr == target: return sorted([hashmap[i][1], hashmap[j][1]])
            if curr < target: i+=1
            else: j-=1
        return sorted([hashmap[i][1], hashmap[j][1]])