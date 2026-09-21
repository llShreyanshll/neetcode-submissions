class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checker = {}

        for i in range(len(nums)):
            if target - nums[i] in checker:
                return [checker[target - nums[i]], i]
            
            checker[nums[i]] = i