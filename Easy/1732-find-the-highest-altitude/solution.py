class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        l=len(gain)
        g=[0]*(l+1)
        for i in range(l):
            g[i+1]=g[i]+gain[i]
        return max(g)
