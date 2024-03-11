class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s), len(p)
        
        # Create a DP table with m+1 rows and n+1 columns
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        # Empty pattern matches empty string
        dp[0][0] = True
        
        # If the pattern starts with '*', it matches empty string
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]
        
        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
                elif p[j - 1] == '?' or s[i - 1] == p[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
        
        return dp[m][n]


sol = Solution()
print(sol.isMatch("aa", "a"))  # Output: False
print(sol.isMatch("aa", "*"))  # Output: True
print(sol.isMatch("cb", "?a")) # Output: False
