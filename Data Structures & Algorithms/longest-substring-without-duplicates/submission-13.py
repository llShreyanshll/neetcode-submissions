class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0,0 
        res = 0
        checker = set()

        while r < len(s):
            while s[r] in checker:
                checker.remove(s[l])
                l += 1
            checker.add(s[r])
            res = max(res, r - l + 1)
            r += 1

        return res