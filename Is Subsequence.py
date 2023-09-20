class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_p = 0

        for i in range(len(t)):
            if s_p == len(s):
                return True
            if t[i] == s[s_p]:
                s_p += 1
        return s_p == len(s)