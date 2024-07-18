class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        return False if str_x != str_x[::-1] else True