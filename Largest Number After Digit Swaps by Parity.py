class Solution:
    def largestInteger(self, num: int) -> int:
        digits = [int(x) for x in str(num)]
        even_digits = [x for x in digits if x % 2 == 0]
        even_digits.sort()
        odd_digits = [x for x in digits if x % 2 == 1]
        odd_digits.sort()

        even_counter = len(even_digits) - 1
        odd_counter = len(odd_digits) - 1
        
        largest_number = ""
        for d in digits:
            if d % 2 == 0:
                largest_number += str(even_digits[even_counter])
                even_counter -= 1
            else:
                largest_number += str(odd_digits[odd_counter])
                odd_counter -= 1
        return int(largest_number)



        


