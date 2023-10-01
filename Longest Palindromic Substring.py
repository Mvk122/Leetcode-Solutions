class Solution:
    def check_palindrome(self, s , l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        l += 1
        r -= 1
        return s[l:r+1]
    

    def longestPalindrome(self, s: str) -> str:
        longest = ""
        for i in range(len(s)):
            o_p = self.check_palindrome(s, i, i)
            if len(o_p) > len(longest):
                longest = o_p
            o_e = self.check_palindrome(s, i, i+1)
            if len(o_e) > len(longest):
                longest = o_e
        return longest


if __name__ == "__main__":
    s = Solution()
    # print(s.longestPalindrome("cbbd"))
    # print(s.longestPalindrome("babad"))
    print(s.longestPalindrome("abb"))