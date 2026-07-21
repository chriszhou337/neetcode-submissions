import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        result = high

        while low <= high:
            median = (low + high) // 2
            eating_time = 0

            for i in range (len(piles)):
                eating_time += math.ceil(float(piles[i] / median))

            if eating_time <= h:
                result = median
                high = median - 1
            else:
                low = median + 1

        return result