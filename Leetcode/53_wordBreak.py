'''
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
'''

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # Create a set for faster lookup
        word_set = set(wordDict)
        # Initialize a boolean array to store if substring ending at index i can be segmented
        dp = [False] * (len(s) + 1)
        dp[0] = True  # Empty string can always be segmented
        for i in range(1, len(s) + 1):
            for j in range(i):
                # If substring ending at index j can be segmented and substring from j to i is in wordDict
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        return dp[-1]
