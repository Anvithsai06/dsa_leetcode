class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        stack=[]
        for i in nums1:
            pos=nums2.index(i)
            while nums2 and pos < len(nums2):
                if nums2[pos]>i:
                    m=nums2[pos]
                    stack.append(m)
                    break
                else:
                    pos+=1
            else:
                stack.append(-1)
        return stack
