class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        dp = [[] for i in range(n + 1)]
        dp[0].append('')
 
        for i in range(n + 1):
            for j in range(i):
                to_be_added = []
                for x in dp[j]:
                    for y in dp[i - j - 1]:
                        to_be_added.append('(' + x + ')' + y)
 
                dp[i] += to_be_added
 
        return dp[n]
