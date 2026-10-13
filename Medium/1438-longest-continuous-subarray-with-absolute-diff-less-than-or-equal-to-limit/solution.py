class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        from collections import deque
        maxq = deque()
        minq = deque()
        l = 0
        ans = 0
        for r in range(len(nums)):
            while maxq and nums[maxq[-1]] < nums[r]:
                maxq.pop()
            maxq.append(r)
            while minq and nums[minq[-1]] > nums[r]:
                minq.pop()
            minq.append(r)
            while nums[maxq[0]] - nums[minq[0]] > limit:
                if maxq[0] == l:
                    maxq.popleft()
                if minq[0] == l:
                    minq.popleft()
                l += 1
            ans = max(ans, r - l + 1)
        return ans
