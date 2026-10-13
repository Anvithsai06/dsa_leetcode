class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l = 0
        ri = 0
        c = 0
        r = []
        max_c = 0

        while ri < len(s):
            if s[ri] in "aeiou":
                c += 1

            if ri - l + 1 == k:
                max_c = max(max_c, c)
                if s[l] in "aeiou":
                    c -= 1
                l += 1

            ri += 1

        return(max_c)
