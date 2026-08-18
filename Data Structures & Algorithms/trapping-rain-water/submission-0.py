class Solution:
    def trap(self, height: List[int]) -> int:

        n = len(height)
        maxL, maxR = 0,0
        left, right = [0]*n, [0]*n
        ans = 0

        for i in range(n):
            j = -i - 1 #cool trick
            left[i] = maxL
            right[j] = maxR
            maxL = max(maxL, height[i])
            maxR = max(maxR, height[j])

        for i in range(n):
            ans += max(0, (min(left[i], right[i]) - height[i]))

        return ans


