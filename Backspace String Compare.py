class Solution:
    def get_str(self, s):
        final = ""
        for char in s:
            if char != "#":
                final += char
            elif len(final) > 0:
                final = final[:-1]
        return final

    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.get_str(s) == self.get_str(t)