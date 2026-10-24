class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack=[]
        count=0
        for i in s:
            if i in '(':
                stack.append(i)
                count+=1
            if i in ')':
                if stack:
                    stack.pop()
                    count-=1
                else:
                    count+=1
        return -1*count if count<0 else count
