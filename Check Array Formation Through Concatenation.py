from typing import List

class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        start_indexes = {}
        for index, piece in enumerate(pieces):
            start_indexes[piece[0]] = index

        piece_ptr = None
        piece_index = 0

        for i, e in enumerate(arr):
            if piece_ptr is None or piece_index == len(pieces[piece_ptr]) - 1:
                if e in start_indexes:
                    piece_ptr = start_indexes[e]
                    piece_index = 0
                    continue
                else:
                    return False
            if e != pieces[piece_ptr][piece_index+1]:
                return False
            piece_index += 1
        return True


if __name__ == "__main__":
    print(Solution().canFormArray([49,18,16], pieces = [[16,18,49]]))
    print(Solution().canFormArray([91,4,64,78], pieces = [[78],[4,64],[91]] ))