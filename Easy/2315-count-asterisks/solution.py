class Solution:
    def countAsterisks(self, s: str) -> int:
        l=s.split("|")
        c=0
        for i in range(0,len(l),2):
            c+=l[i].count("*")

        return c
