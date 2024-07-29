class Solution:
    def subtractive_form(self, num, multiply, standard_numbers):
        tmp = (num // multiply) * multiply
        roman_str = ""

        while tmp >= multiply:
            if tmp in standard_numbers:
                roman_str += standard_numbers[tmp]
                break
            else:
                previous_val = None
                for key in standard_numbers.keys():
                    if previous_val and key > tmp and tmp in range(multiply, multiply*10):
                        roman_str += standard_numbers[previous_val]
                        tmp = tmp - previous_val
                        break

                    previous_val = key
        return roman_str
                    
    def intToRoman(self, num: int) -> str:
        standard_numbers = {
            1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50: "L",
            90: "XC", 100: "C", 400: "CD", 500: "D", 900: "CM", 1000: "M"
        }

        roman_str = ""
        current_num = num

        if current_num >= 1000:
            roman_str += f"{(current_num // 1000) * standard_numbers[1000]}"
            current_num = current_num % 1000

        if current_num >= 100:
            roman_str += f"{self.subtractive_form(current_num, 100, standard_numbers)}"
            current_num = current_num % 100

        if current_num >= 10:
            roman_str += f"{self.subtractive_form(current_num, 10, standard_numbers)}"
            current_num = current_num % 10

        if current_num >= 1:
            roman_str += f"{self.subtractive_form(current_num, 1, standard_numbers)}"
            current_num = current_num % 1

        return roman_str
    

####################################################
##################### OPTION 2 #####################
####################################################

class Solution:
    def intToRoman(self, num: int) -> str:
        standard_numbers = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), 
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"), 
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]
        
        roman_str = ""
        for value, symbol in standard_numbers:
            while num >= value:
                roman_str += symbol
                num -= value

        return roman_str
