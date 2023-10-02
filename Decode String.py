class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i, c in enumerate(s):
            if c != "]":
                stack.append(c)
            else:
                current = []
                while stack[-1] != "[":
                    current.append(stack.pop())
                a = stack.pop() # Removing the [
                nums = []
                while stack and stack[-1].isdigit():
                    nums.append(stack.pop())

                amount = int(''.join(reversed(nums)))
                stack.append(''.join(reversed(current)) * amount)
        return ''.join(stack)