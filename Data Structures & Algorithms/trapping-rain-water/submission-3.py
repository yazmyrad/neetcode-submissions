class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        stack, lmax, rmax = [], [height[0]], [0]*n
        rmax[-1] = height[-1]
        for i in range(n-2, -1, -1):
            rmax[i] = max(rmax[i+1], height[i])
       
        for i in range(1, n):
            lmax.append(max(lmax[-1], height[i]))

        ans = 0
        for i in range(n):
            r, l = rmax[i], lmax[i]
            vol = min(r, l) - height[i]
            if vol > 0:
                ans += vol
        return ans
