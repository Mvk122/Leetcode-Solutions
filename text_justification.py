from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines = []
        current_letters = 0
        l = 0
        
        for i, word in enumerate(words):
            if len(word) + current_letters > maxWidth:
                lines.append(self.justify_sentence(words[l:i], maxWidth))
                l = i
                current_letters = len(word) + 1
            else:
                current_letters += 1 + len(word)

        lines.append(self.justify_final_sentence(words[l:], maxWidth))

        return lines

    def justify_sentence(self, words, maxWidth):
        if len(words) == 1:
            return words[0] + (" " * (maxWidth - len(words[0])))
        
        letter_count = 0
        for word in words:
            letter_count += len(word)

        spaces_to_use = (maxWidth - letter_count) // (len(words)-1)
        remaining = (maxWidth - letter_count) % (len(words)-1)
        final_sentence = ""

        for word in words[:-1]:
            final_sentence += word + (" " * spaces_to_use)
            if remaining > 0:
                final_sentence += " "
                remaining -= 1

        final_sentence += words[-1]

        return final_sentence



    def justify_final_sentence(self, words, maxWidth):
        final = " ".join(words)
        final += " " * (maxWidth - len(final))
        return final
    

s = Solution()
# print(s.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16))
print(s.fullJustify(["What","must","be","acknowledgment","shall","be"], maxWidth = 16))
