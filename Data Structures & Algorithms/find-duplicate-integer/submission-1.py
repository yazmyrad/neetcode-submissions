class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dup = 0

        for x in nums:
            b = 1<<x
            nexts = dup ^ b

            if nexts < dup:
                return x

            dup = nexts