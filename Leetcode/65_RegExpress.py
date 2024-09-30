'''
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

 

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
'''

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # dp[i][j] will be True if the first i characters of s match the first j characters of p
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        
        # Empty string matches with empty pattern
        dp[0][0] = True
        
        # Handle patterns like "a*", "a*b*", etc., which can match an empty string
        for j in range(2, len(p) + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        # Fill the dp table
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                    # Current characters match
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    # Two cases for '*'
                    # Case 1: Treat '*' as matching zero of the previous character
                    dp[i][j] = dp[i][j - 2]
                    # Case 2: Treat '*' as matching one or more of the previous character
                    if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
        
        return dp[len(s)][len(p)]




'''

To solve this problem, we can use dynamic programming (DP) to simulate the process of matching the string s with the pattern p considering the special characters . and *.

Dynamic Programming Approach:
We can define a 2D boolean array dp where dp[i][j] will be True if the first i characters of s match the first j characters of p.

The steps are:

If p[j-1] is a . or s[i-1] == p[j-1], then the current characters match, and dp[i][j] = dp[i-1][j-1].
If p[j-1] is a *, it can act in two ways:
Match zero occurrences of the character before *: dp[i][j] = dp[i][j-2].
Match one or more occurrences of the character before *: dp[i][j] = dp[i-1][j] (if the character before * matches s[i-1] or is a .).
Python Implementation:
python
Copia el codi
def isMatch(s: str, p: str) -> bool:
    # dp[i][j] will be True if the first i characters of s match the first j characters of p
    dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
    
    # Empty string matches with empty pattern
    dp[0][0] = True
    
    # Handle patterns like "a*", "a*b*", etc., which can match an empty string
    for j in range(2, len(p) + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 2]

    # Fill the dp table
    for i in range(1, len(s) + 1):
        for j in range(1, len(p) + 1):
            if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                # Current characters match
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == '*':
                # Two cases for '*'
                # Case 1: Treat '*' as matching zero of the previous character
                dp[i][j] = dp[i][j - 2]
                # Case 2: Treat '*' as matching one or more of the previous character
                if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                    dp[i][j] = dp[i][j] or dp[i - 1][j]
    
    return dp[len(s)][len(p)]
Explanation:
Base Case: The empty string matches with an empty pattern (dp[0][0] = True).
Pre-fill for Patterns with *: Patterns like "a*" can match an empty string, so we handle these cases.
Filling the dp Table:
If the current characters match (. or the same character), we propagate the result from the previous state.
If the pattern contains *, we handle two cases: zero occurrences or one/more occurrences of the previous character.
'''