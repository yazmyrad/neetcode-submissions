class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums)-1
        while i >= 0 and j <= len(nums)-1 and i <= j:
            mid = int((i+j)/2)
            if nums[mid] == target: 
                return mid
            elif i == j and nums[i] != target:
                return -1
            elif nums[mid] > target:
                j = mid-1
            else:
                i = mid+1
        return -1 if nums[i] != target else i