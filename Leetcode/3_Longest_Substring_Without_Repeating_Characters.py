'''
Given a string s, find the length of the longest substring without repeating characters.
 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.


Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_index_map = {}
        max_length = 0
        start = 0
        
        for end in range(len(s)):
            if s[end] in char_index_map:
                # Move start pointer to the right of the last occurrence of the character
                start = max(start, char_index_map[s[end]] + 1)
            # Update the index of the current character
            char_index_map[s[end]] = end
            # Update the maximum length if needed
            max_length = max(max_length, end - start + 1)
        
        return max_length

# Example usage:
solution = Solution()
print(solution.lengthOfLongestSubstring("abcabcbb"))  # Output: 3
print(solution.lengthOfLongestSubstring("bbbbb"))     # Output: 1
print(solution.lengthOfLongestSubstring("pwwkew"))    # Output: 3
