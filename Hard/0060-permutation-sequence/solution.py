class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums=[]
        for i in range(1,n+1):
            nums.append(str(i))
        fact = [1]*(n+1)
        for i in range(1,n+1):
            fact[i]=fact[i-1]*i
        k-=1
        ans=''
        for i in range(n,0,-1):
            idx = k//fact[i-1]
            ans += nums[idx]
            nums.pop(idx)
            k%=fact[i-1]
        return ans
