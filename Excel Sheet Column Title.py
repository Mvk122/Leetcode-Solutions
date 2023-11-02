class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        current = columnNumber
        current_string = ""

        while current != 0:
            current -= 1
            remainder = current % 26
            current_string = chr(65+remainder) + current_string
            current = current // 26
        return current_string