from typing import List

class Solution:
    def permute(self, remainder, result, mapping, current):
        if remainder == "":
            if current != "":
                result.append(current)
        else:
            for element in mapping[remainder[0]]:
                self.permute(remainder[1:], result, mapping, current+element)
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            "2": ["a", 'b', 'c'],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", 'n', 'o'],
            "7": ['p', 'q', 'r', 's'],
            "8": ['t', 'u', 'v'],
            "9": ["w", "x", "y", "z"]
        }
        result = []
        self.permute(digits, result, mapping, "")
        return result
