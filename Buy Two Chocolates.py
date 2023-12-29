from typing import List

class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        first_smallest = float('inf')
        second_smallest = float('inf')

        for price in prices:
            if price <= first_smallest:
                second_smallest = first_smallest
                first_smallest = price
            elif price < second_smallest: 
                second_smallest = price

        if first_smallest + second_smallest <= money:
            return money - (first_smallest + second_smallest)
        
        return money