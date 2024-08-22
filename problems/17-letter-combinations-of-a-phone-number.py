class Solution:
    def brute_force_merge(self, current_list, next_digit_list) -> list:
        merged_list = []

        for i in current_list:
            for j in next_digit_list:
                merged_list.append(i+j)

        return merged_list

    def letterCombinations(self, digits: str) -> List[str]:
        chars_number = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        if len(digits) == 0:
            return []
        
        if len(digits) < 2:
            return chars_number[digits]
            
        i = 0
        merged_list = []
        while i < len(digits)-1:
            second_number = chars_number[digits[i+1]]

            if not merged_list:
                first_number = chars_number[digits[i]]
                merged_list = self.brute_force_merge(first_number, second_number)
            else:
                merged_list = self.brute_force_merge(merged_list, second_number)

            i += 1

        return merged_list

