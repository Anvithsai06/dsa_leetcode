class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        l=s.split()
        for i in range(k+1):
            l+=l.pop(0)
        return "".join(l)
