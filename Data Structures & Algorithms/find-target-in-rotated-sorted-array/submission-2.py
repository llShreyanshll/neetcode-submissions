class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m

        min_i = l

        if nums[0] <= nums[len(nums)-1]:
            l, r = 0, len(nums) - 1
        elif nums[0] <= target and target <= nums[min_i - 1]:
            l, r = 0, min_i - 1
        else:
            l, r = min_i, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1


        




        