class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            hashmap[num] = i
        
        for j, num in enumerate(nums):
            diff = target - num
            if diff in hashmap and j != hashmap[diff]:
                return [j, hashmap[diff]]