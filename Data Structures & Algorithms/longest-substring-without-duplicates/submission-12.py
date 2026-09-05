class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        checker = set()
        res = 0

        while r < len(s):
            while s[r] in checker:
                checker.remove(s[l])
                l += 1

            checker.add(s[r])
            r += 1
            res = max(res, r - l)

        return res 