class Solution:
    def firstUniqChar(self, s: str) -> int:
        l=[]
        for i in s:
            l.append(s.count(i))
        m=min(l)
        if m<=1:
            m =l.index(m)
        else:
            m=-1
        return m
