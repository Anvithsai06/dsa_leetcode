class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        count = 0
        l = len(s)
        for i in range(l):
            if s[i] in t:
                t = t[t.index(s[i]) + 1:]
                count += 1
            else:
                return False
        return count == l
