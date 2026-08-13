class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydict = {}
        for i in range(len(nums)):
            a = target - nums[i]
            if a in mydict:
                return sorted([i, mydict[a]])

            mydict[nums[i]] = i

        
            