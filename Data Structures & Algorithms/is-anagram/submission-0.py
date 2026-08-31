class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dic = {}
        t_dic = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            s_dic[s[i]] = s_dic.get(s[i], 0) + 1
            t_dic[t[i]] = t_dic.get(t[i], 0) + 1

        return s_dic == t_dic