class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        """for i in range(len(s)-1,0,-1):
            if s[i] in "aeiou":
                s=s[:i]
                print(s)
            else:
                s=s[:i+1]
                return "" if s == null else s"""
        i = len(s) - 1
        while i >= 0 and s[i] in "aeiou":
            i -= 1
        return s[:i+1]
