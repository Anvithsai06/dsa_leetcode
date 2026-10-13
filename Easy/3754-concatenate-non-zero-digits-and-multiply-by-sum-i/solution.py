class Solution:
    def sumAndMultiply(self, n: int) -> int:
        a=""
        s=0
        n=str(n)
        for i in n:
            if i!="0":
                a+=i
                s+=int(i)
        x=int(a) if a else 0
        x=x*s
        return x
