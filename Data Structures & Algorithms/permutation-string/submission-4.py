class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        checker1 = {}
        checker2 = {}
        l, r = 0, len(s1) - 1
        for i in range(len(s1)):
            checker1[s1[i]] = checker1.get(s1[i], 0) + 1
        for i in range(len(s1) - 1):
            checker2[s2[i]] = checker2.get(s2[i], 0) + 1

        while r < len(s2):
            checker2[s2[r]] = checker2.get(s2[r], 0) + 1

            if checker1 == checker2:
                return True

            checker2[s2[l]] -= 1
            if checker2[s2[l]] == 0:
                checker2.pop(s2[l])

            r += 1
            l += 1

        return False