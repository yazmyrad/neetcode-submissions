class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        def findinsorted(i, j):
            while i<=j:
                mid = (i+j)//2
                if nums[mid] == target: return mid
                if nums[mid] < target: i = mid + 1
                else: j = mid - 1
            return -1 
        mid = (r-l)//2
        while l < r:
            mid = (l+r)//2
            if nums[mid] > nums[r]: l = mid+1
            else: r = mid
        mid = l
        res = findinsorted(0, mid-1)
        if res!= -1:
            return res
        return findinsorted(mid, len(nums)-1)