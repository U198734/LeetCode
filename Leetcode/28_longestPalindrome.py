class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return ""
        
        n = len(s)
        # Create a table to store if substrings are palindromes
        dp = [[False] * n for _ in range(n)]
        
        start, max_length = 0, 1
        
        # All substrings of length 1 are palindromes
        for i in range(n):
            dp[i][i] = True
        
        # Check for substrings of length 2
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                start = i
                max_length = 2
        
        # Check for substrings of length more than 2
        for length in range(3, n+1):
            for i in range(n-length+1):
                j = i + length - 1
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    start = i
                    max_length = length
        
        return s[start:start+max_length]

# Example usage:
solution = Solution()
print(solution.longestPalindrome("babad"))  # Output: "bab" or "aba"
print(solution.longestPalindrome("cbbd"))   # Output: "bb"
