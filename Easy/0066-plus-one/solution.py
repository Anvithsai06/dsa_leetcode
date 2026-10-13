class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        d=""
        for i in digits:
            d+=str(i)
        d=int(d)+1
        d=str(d)
        return [int(x) for x in d]
