class Solution:
    def __init__(self):
        self.valid_parentheses = ['{}', '[]', '()']

    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        
        parentheses = []
        for idx in range(len(s)):
            parentheses.append(s[idx])

            if len(parentheses) > 1:
                tmp_parentheses = parentheses[-2] + parentheses[-1]
                if tmp_parentheses in self.valid_parentheses:
                    parentheses.pop(-1) # remove last (eg. ']')
                    parentheses.pop(-1) # remove second last  (eg. '[')

        return True if len(parentheses) == 0 else False

        
                
