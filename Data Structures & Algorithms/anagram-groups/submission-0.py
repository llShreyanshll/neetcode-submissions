class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}

        for c in strs:
            count = [0] * 26
            for s in c:
                count[ord(s) - ord('a')] += 1
            key = tuple(count)
            result[key] = result.get(key, [])
            result[key].append(c)
        return list(result.values())