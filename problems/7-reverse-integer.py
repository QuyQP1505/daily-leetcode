class Solution:
    def reverse(self, x: int) -> int:
        str_int = str(x)
        result = 0
        if "-" in str_int:
            _, value = str_int.split("-")
            result = int("".join(["-", value[::-1]]))
        else:
            result = int(str_int[::-1])

        if result in range((-2)**31, (2)**31):
            return result
        else:
            return 0