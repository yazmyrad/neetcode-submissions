# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        n = len(pairs)
        if n == 0:
            return pairs
        states = [pairs[::]]
        for i in range(1, n):
            pair = pairs[i]
            j = i - 1
            while j >= 0 and pair.key < pairs[j].key:
                pairs[j+1] = pairs[j]
                j -= 1
            pairs[j+1] = pair
            states.append(pairs[::])
        #states.append(pairs[::])
        return states
