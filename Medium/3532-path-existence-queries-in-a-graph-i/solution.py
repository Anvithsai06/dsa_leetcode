class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        group = [0] * n
        g = 0
        for i in range(1, n):
            if nums[i] - nums[i - 1] > maxDiff:
                g += 1
            group[i] = g
        ans = []
        for u, v in queries:
            if group[u] == group[v]:
                ans.append(True)
            else:
                ans.append(False)
        return ans
