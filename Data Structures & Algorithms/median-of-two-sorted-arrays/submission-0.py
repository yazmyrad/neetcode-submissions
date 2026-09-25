class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        m, n = len(nums1), len(nums2)
        total = m + n
        half = total // 2
        l, r = 0, m - 1
        
        while True:
            midA = (l + r) // 2
            midB = half - (midA + 1) - 1
            
            a1 = nums1[midA] if midA >= 0 else float('-inf')
            a2 = nums1[midA + 1] if (midA + 1) < m else float('inf')
            
            b1 = nums2[midB] if midB >= 0 else float('-inf')
            b2 = nums2[midB + 1] if (midB + 1) < n else float('inf')
            
            if a1 <= b2 and b1 <= a2:
                if total % 2 != 0:
                    return min(a2, b2)
                return (max(a1, b1) + min(a2, b2)) / 2
                
            elif a1 > b2:
                r = midA - 1
            else:
                l = midA + 1
