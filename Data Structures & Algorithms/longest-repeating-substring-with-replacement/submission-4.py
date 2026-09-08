class Solution:

    def characterReplacement(self, s: str, k: int) -> int:
        checker = {}
        l, r = 0, 0
        res = 0

        while r < len(s):
            checker[s[r]] = checker.get(s[r], 0) + 1
            if (r - l + 1) - max(checker.values()) > k:
                checker[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
            r += 1

        return res
                
                    


