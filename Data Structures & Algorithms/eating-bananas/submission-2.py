class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxpiles = max(piles)
        r, l = 1, maxpiles
        k = r + (l-r)//2
        mink = maxpiles
        while r <= l:
            time = 0
            for pile in piles:
                time += pile // k + (pile % k > 0)
            #print(k, time, r, l, mink)
            if time <= h:
                l = k - 1
                mink = min(k, mink)
            else:
                r = k + 1
            k = r + (l-r)//2
        print(mink)
        #mink = min(k, mink)
        return mink 