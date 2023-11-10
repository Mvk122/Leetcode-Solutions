from typing import List

class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        current_character = None
        current_character_count = 1
        large_groups = []

        for index, character in enumerate(s):
            if character != current_character:
                if current_character_count >= 3:
                    large_groups.append([index-current_character_count, index-1])
                current_character = character
                current_character_count = 1
            else:
                current_character_count += 1
        
        if current_character_count >= 3:
            large_groups.append([len(s)-current_character_count, len(s)-1])
        return large_groups
