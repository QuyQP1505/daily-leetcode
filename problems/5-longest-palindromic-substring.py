class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s[::-1] == s:
            return s

        start = 0
        palind_dict = {}
        for idx, char in enumerate(s):
            longest_palind = ""
            for jdx in range(idx, len(s)):
                longest_palind += s[jdx]  
                if longest_palind == longest_palind[::-1]:
                    palind_dict[longest_palind] = len(longest_palind)
        
        result = sorted(palind_dict.items(), key=lambda x: x[1])[-1][0]
        return result
                    
