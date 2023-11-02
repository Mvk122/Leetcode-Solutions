class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        start_pointer = 0
        remove_indices = set()
        for index, element in enumerate(s):
            if element == "(":
                if len(stack) == 0:
                    start_pointer = index
                stack.append("(")
            elif element == ")":
                if stack[-1] == "(":
                    stack.pop()
            if len(stack) == 0:
                remove_indices.add(index)
                remove_indices.add(start_pointer)
        final = ""
        for index, element in enumerate(s):
            if index not in remove_indices:
                final += element
        return final