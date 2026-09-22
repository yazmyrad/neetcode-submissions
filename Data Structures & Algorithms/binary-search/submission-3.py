class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums)
        while i < j:
            mid = i+(j-i)//2
            if nums[mid] >= target:
                j = mid
            else:
                i = mid+1
        return i if i < len(nums) and nums[i] == target else -1