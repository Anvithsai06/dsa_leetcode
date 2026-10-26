class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        j=m
        for i in nums2:
            nums1[j]=i
            j+=1
        nums1.sort()
