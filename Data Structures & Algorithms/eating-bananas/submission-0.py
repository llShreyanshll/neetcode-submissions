import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            rate = (l + r) // 2

            hours = 0
            for pile in piles:
                hours += math.ceil(pile/rate)

            if hours <= h:
                res = min(res, rate)
                r = rate - 1
            else:
                l = rate + 1

        return res


