class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_exists = list(set(s))

        new_dict = {}
        for char in char_exists:
            new_dict[char] = 0


