class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}

        for index, num in enumerate(nums):
            a = target - num
            if a in dic:
                return [dic[a], index]

            else:
                dic[num] = dic.get(num, index)