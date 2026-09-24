class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0] 
        elif nums[0] < nums[1] and nums[0] < nums[n-1]:
            return nums[0]
        r, l = 0, n-1
        while r<=l:
            mid = r + (l-r)//2
            print(mid, r, l, nums[mid])
            if mid > 0 and nums[mid-1] > nums[mid]:
                return nums[mid]
            elif nums[r] > nums[mid]:
                l = mid - 1
            elif nums[l] < nums[mid]:
                r = mid + 1
            elif nums[r-1] > nums[r]:
                return nums[r]
        return nums[r]