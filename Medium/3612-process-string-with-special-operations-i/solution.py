class Solution(object):
    def processStr(self, s):
        """
        :type s: str
        :rtype: str
        """
        l=''
        for i in s:
            if i>='a' and i<='z':
                l+=i
            if i == '*':
                l=l[:-1]
            if i == '#':
                l=l+l[:]
            if i == '%':
                l=l[::-1]
        return l
            
                
