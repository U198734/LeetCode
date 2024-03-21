'''
Given a string s consisting only of characters 'a', 'b', and 'c'. You are asked to apply the following algorithm on the string any number of times:

Pick a non-empty prefix from the string s where all the characters in the prefix are equal.
Pick a non-empty suffix from the string s where all the characters in this suffix are equal.
The prefix and the suffix should not intersect at any index.
The characters from the prefix and suffix must be the same.
Delete both the prefix and the suffix.
Return the minimum length of s after performing the above operation any number of times (possibly zero times).

 

Example 1:

Input: s = "ca"
Output: 2
Explanation: You can't remove any characters, so the string stays as is.
Example 2:

Input: s = "cabaabac"
Output: 0
Explanation: An optimal sequence of operations is:
- Take prefix = "c" and suffix = "c" and remove them, s = "abaaba".
- Take prefix = "a" and suffix = "a" and remove them, s = "baab".
- Take prefix = "b" and suffix = "b" and remove them, s = "aa".
- Take prefix = "a" and suffix = "a" and remove them, s = "".
Example 3:

Input: s = "aabccabba"
Output: 3
Explanation: An optimal sequence of operations is:
- Take prefix = "aa" and suffix = "a" and remove them, s = "bccabb".
- Take prefix = "b" and suffix = "bb" and remove them, s = "cca".
 
'''

class Solution(object):
    def minimumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Initialize left and right pointers
        left, right = 0, len(s) - 1
        
        # Loop while there are still characters in the string
        while left < right:
            # If left and right characters are the same, find the whole segment and remove it
            if s[left] == s[right]:
                current_char = s[left]
                while left <= right and s[left] == current_char:
                    left += 1
                while right >= left and s[right] == current_char:
                    right -= 1
            else:
                # If left and right characters are different, stop the loop
                break
        
        # After the loop, check if left pointer passed right pointer, return 0 if so
        return max(0, right - left + 1)

# Example usage:
solution = Solution()
print(solution.minimumLength("ca"))      # Output: 2
print(solution.minimumLength("cabaabac")) # Output: 0
print(solution.minimumLength("aabccabba"))# Output: 3
