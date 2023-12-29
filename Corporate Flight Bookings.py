from typing import List


class Solution:
    def corpFlightBookings_slow(self, bookings: List[List[int]], n: int) -> List[int]:
        ret = [0 for _ in range(n)]
        for booking in bookings:
            for i in range(booking[0]-1, booking[1]):
                ret[i] += booking[2]
        return ret
    
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ret = [0 for _ in range(n+1)]

        for booking in bookings:
            ret[booking[0]-1] += booking[2]
            if booking[1] < n:
                ret[booking[1]] -= booking[2]

        for i in range(1, n):
            ret[i] += ret[i-1]
        
        ret.pop()
        return ret        