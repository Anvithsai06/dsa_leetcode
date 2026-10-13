class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x=str(x)
        if x[0]=='-':
            f= int('-'+x[:0:-1])
        else:
            f= int(x[::-1])
        if -2**31 <= f <= (2**31) -1:
            return f
        else:
            return 0
