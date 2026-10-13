class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        l=len(s)
        flag=False
        for i in range(l):
            if s == goal:
                flag=True
            ls=s[0]
            s=s[1:]+ls
        return flag
