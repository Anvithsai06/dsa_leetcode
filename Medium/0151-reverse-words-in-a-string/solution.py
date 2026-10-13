class Solution:
    def reverseWords(self, s: str) -> str:
        words=s.strip().split()[::-1]
        out=""
        for i in words:
            out+=" "
            out+=i
        return out.strip()
