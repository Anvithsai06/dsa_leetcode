class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """l=[]
        s,i=len(nums),0
        while i<=range(s):
            if nums[i]==target:
                l.append(i)
            i+=1
        return l if l!=[] else [-1,-1]"""


        """def bin(nums,low,high,target,l):
            mid=(high+low)//2
            if nums[mid]!=target:
                if nums[mid] < target:
                    bin(nums,low,mid,target,l)
                else:
                    bin(nums,mid,high,target,l)
            else:
                return l.append(mid)
        high=len(nums)
        low=0
        l=[]
        bin(nums,low,high,target,l)
        return l if l!=[] else [-1,-1]"""

        result=[]
        if target not in nums or len(nums)==0:
            return [-1,-1]
        a=[]
        a.append(nums.index(target))
        b=nums[::-1]
        x=(len(nums)-1)-(b.index(target))
        a.append(x)
        return a
