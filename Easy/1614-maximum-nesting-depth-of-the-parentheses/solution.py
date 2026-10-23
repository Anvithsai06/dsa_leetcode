class Solution:
    def maxDepth(self, s: str) -> int:
        count,m=0,0
        stack=[]
        for i in s:
            if i in '(':
                stack.append(i)
                count+=1
                m=max(m,count)
            elif i in ')':
                stack.pop()
                count-=1
        return m
