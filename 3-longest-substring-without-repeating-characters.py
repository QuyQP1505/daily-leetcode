class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_exists = list(set(s))

        longest_char = []
        tmp_longest_string = ""
        for idx, char in enumerate(s):
            while tmp_longest_string[-1] != s[idx]:
                tmp_longest_string += s[idx]

            longest_char.append(tmp_longest_string)

        return len(sorted(longest_char)[-1])
