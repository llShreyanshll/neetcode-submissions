class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) == 0:
            return ""

        countT = {}
        window = {}

        for i in range(len(t)):
            countT[t[i]] = 1 + countT.get(t[i], 0)

        have, need = 0, len(countT)                  #l X[6]
                                                #r V [9]
        ans = (0, 0)                            #countT: X:1, Y:1, Z:1
        ansLen = float("infinity")              #window O:1, U: 1, Z:3
                                                #have = 2
                                                #ansLen = 4, l=6, r=8
                                                #ans = (5,8)
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and countT[c] == window[c]:
                have += 1

            while have == need:
                if (r - l + 1) < ansLen:
                    ansLen = r - l + 1
                    ans = (l, r)

                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1

                #window[s[l]] -= 1
                l += 1
        l, r = ans
        return s[l:r+1] if ansLen != float("infinity") else ""