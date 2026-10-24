class Solution:
    def validateStackSequences(self, pushed: list[int], popped: list[int]) -> bool:
        stack=[]
        for i in pushed:
            stack.append(i)
            while stack and stack[-1] == popped[0]:
                stack.pop()
                popped.pop(0)
        return len(stack)==0
