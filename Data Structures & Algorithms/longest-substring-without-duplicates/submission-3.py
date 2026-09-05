class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        checker = {}
        res = 0
        if not s:
            return 0
        while r < len(s):
            if s[r] not in checker:
                checker[s[r]] = checker.get(s[r], 0) + 1
                res = max(res, r - l)
                r += 1
            else:
                while s[r] in checker:
                    del checker[s[l]]
                    l += 1

        return res + 1

                
                
        
        