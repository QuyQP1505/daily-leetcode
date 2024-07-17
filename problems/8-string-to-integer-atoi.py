class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0

        sign = 1
        i = 0
        if s[i] in ["-", "+"]:
            if s[i] == "-":
                sign = -1
            i += 1

        result = 0
        while i < len(s) and s[i].isdigit():
            result = result * 10 + int(s[i])
            i += 1

        result *= sign
        int_max, int_min = 2**31 - 1, -2**31

        if result < int_min:
            return int_min
        if result > int_max:
            return int_max

        return result
