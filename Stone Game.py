from typing import List


class Solution:
    # Greedy solution doesn't always work
    def stoneGame_greedy(self, piles: List[int]) -> bool:
        alice_turn = True
        alice_amount = 0
        bob_amount = 0

        start_pointer = 0
        end_pointer = len(piles) - 1

        while start_pointer < end_pointer:
            if piles[start_pointer] > piles[end_pointer]:
                current_amount = piles[start_pointer]
                start_pointer += 1
            else:
                current_amount = piles[end_pointer]
                end_pointer -= 1

            if alice_turn:
                alice_amount += current_amount
            else:
                bob_amount += current_amount

            alice_turn = not alice_turn

        return alice_amount > bob_amount