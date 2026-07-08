class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = set()
        l, r = 0,0
        ans = 0
        
        while l <= r and r < len(s):
            if s[r] not in res:
                res.add(s[r])
                r += 1
            elif s[r] in res:
                res.remove(s[l])
                l += 1
            ans = max(ans, len(res))

        return ans