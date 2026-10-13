class Solution:
    def smallestPalindrome(self, s: str) -> str:
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - ord('a')] += 1
        half = []
        mid = ""
        for i in range(26):
            half.append(chr(i + ord('a')) * (cnt[i] // 2))
            if cnt[i] % 2 == 1:
                mid = chr(i + ord('a'))
        left = "".join(half)
        return left + mid + left[::-1]
