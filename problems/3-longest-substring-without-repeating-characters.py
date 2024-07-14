class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        start = 0
        max_length = 0
        char_index_map = {}

        for idx, char in enumerate(s):
            if char in char_index_map:
                if char_index_map[char] >= start:
                    start = char_index_map[char] + 1
            
            char_index_map[char] = idx
            max_length = max(max_length, idx - start + 1)
        
        return max_length
