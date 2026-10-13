class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        from typing import List
        total_xor = 0
        zero_count = 0

        for x in nums:
            total_xor ^= x
            if x == 0:
                zero_count += 1

        n = len(nums)

        if total_xor != 0:
            return n

        if zero_count == n:
            return 0

        return n - 1
