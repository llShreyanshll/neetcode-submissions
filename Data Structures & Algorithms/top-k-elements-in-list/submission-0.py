class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:   
        counter = {}

        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        res = [[] for i in range(len(nums) + 1)] 

        for num, freq in counter.items():
            res[freq].append(num)

        ans = []
        for i in range((len(res) - 1), -1, -1):
            for j in res[i]:
                ans.append(j)
                if len(ans) == k:
                    return ans
