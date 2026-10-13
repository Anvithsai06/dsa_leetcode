class Solution:
    def convertToBase7(self, num: int) -> str:
        result = ""
        if num<0:
            temp="-" 
        elif num >0:
            temp = ""
        else:
            return "0"
        num=abs(num)
        while num!=0:
            result= str(num%7) + result
            num=num//7
        return temp+result
