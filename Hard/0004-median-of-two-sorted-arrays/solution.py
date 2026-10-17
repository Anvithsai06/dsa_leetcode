class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums1.extend(nums2)
        nums1=sorted(nums1)
        l=len(nums1)
        mid=l//2
        if l%2==0:
            return (nums1[mid-1]+nums1[mid])/2
        else:
            return nums1[mid]
