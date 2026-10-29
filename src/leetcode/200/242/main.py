class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        n = len(s)
        s_dict = {}
        t_dict = {}
        for i in range(n):
            if s[i] in s_dict:
                s_dict[s[i]] += 1
            else:
                s_dict[s[i]] = 1
            if t[i] in t_dict:
                t_dict[t[i]] += 1
            else:
                t_dict[t[i]] = 1
        for k, v in s_dict.items():
            if not k in t_dict:
                return False
            if v != t_dict[k]:
                return False
        return True
