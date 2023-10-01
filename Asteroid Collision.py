from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        final =  []
        for asteroid in asteroids:
            destroyed = False
            appended = False
            while len(final) > 0:

                if asteroid * final[-1] > 0:
                    final.append(asteroid)
                    appended = True
                    break
                elif final[-1] < 0 and asteroid > 0:
                    final.append(asteroid)
                    appended = True
                    break

                if abs(asteroid) == abs(final[-1]):
                    final.pop()
                    destroyed = True
                    break
                elif abs(asteroid) > abs(final[-1]):
                    final.pop()
                    continue 
                else:
                    destroyed = True
                    break
                

            if (not destroyed) and (not appended):
                final.append(asteroid)

        return final