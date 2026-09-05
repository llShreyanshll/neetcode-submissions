class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        checker = set()
        res = 0

        while r < len(s):
            if s[r] not in checker:
                checker.add(s[r])
                r += 1
            else:
                while s[r] in checker:
                    checker.remove(s[l])
                    l += 1
            res = max(res, r - l)

        return res

                
                
        
        