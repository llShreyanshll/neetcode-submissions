from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0
        l, r = 0, 0
        count = defaultdict(int)

        while l <= r and r < len(s):
            count[s[r]] += 1
            most_freq = max(count.values())
            window = (r - l) + 1
            if window - most_freq <= k:
                ans = max(ans, window)
                r += 1
            else:
                while window - most_freq > k:
                    count[s[l]] -= 1
                    l += 1
                    
                    most_freq = max(count.values())
                    window = (r - l) + 1
                r += 1
        return ans

