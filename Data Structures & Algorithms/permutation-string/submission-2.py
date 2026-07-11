class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ss1 = {}
        ss2 = {}
        for i in range(len(s1)):
            ss1[s1[i]] = 1 + ss1.get(s1[i], 0)

        l = 0 

        for i in range(len(s2)):

            ss2[s2[i]] = 1 + ss2.get(s2[i], 0)

            while sum(ss2.values()) > sum(ss1.values()):
                ss2[s2[l]] -= 1
                if ss2[s2[l]] == 0:
                    ss2.pop(s2[l])
                l += 1

            

            print(sum(ss2.values()))

            #print("ss2 :", ss2)
            #print("ss1 :",ss1)

            if ss2 == ss1:
                return True
        return False
      