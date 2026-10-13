class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        text=sorted(text)
        s=set(text)
        x=[]
        for i in s:
            if i in "balloon":
                c=text.count(i)
                if i in "lo":
                    x.append(c//2)
                else:
                    x.append(c)
        return min(x) if x and min(x)>0 and len(x)==5 else 0
