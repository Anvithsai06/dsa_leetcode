class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last = {}
        for i in range(len(s)):
            last[s[i]] = i

        stack = []
        seen = set()

        for i in range(len(s)):
            c = s[i]

            if c in seen:
                continue

            while stack and c < stack[-1] and last[stack[-1]] > i:
                seen.remove(stack.pop())

            stack.append(c)
            seen.add(c)

        return "".join(stack) 
