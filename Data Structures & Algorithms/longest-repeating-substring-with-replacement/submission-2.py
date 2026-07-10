class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        counter = {}
        l, r = 0, 0
        ans = 0

        while l <=r and r < len(s):

            counter[s[r]] = 1 + counter.get(s[r], 0)
            while (r - l + 1) - max(counter.values()) > k:
                counter[s[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)
            r += 1

        return ans














    
