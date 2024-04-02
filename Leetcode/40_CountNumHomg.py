'''
- Count Number of Homogenous Substrings

Given a string s, return the number of homogenous substrings of s. Since the answer may be too large, return it modulo 109 + 7.

A string is homogenous if all the characters of the string are the same.

A substring is a contiguous sequence of characters within a string.

 

Example 1:

Input: s = "abbcccaa"
Output: 13
Explanation: The homogenous substrings are listed as below:
"a"   appears 3 times.
"aa"  appears 1 time.
"b"   appears 2 times.
"bb"  appears 1 time.
"c"   appears 3 times.
"cc"  appears 2 times.
"ccc" appears 1 time.
3 + 1 + 2 + 1 + 3 + 2 + 1 = 13.
Example 2:

Input: s = "xy"
Output: 2
Explanation: The homogenous substrings are "x" and "y".
Example 3:

Input: s = "zzzzz"
Output: 15

'''

class Solution(object):
    def countHomogenous(self, s):
        """
        :type s: str
        :rtype: int
        """
        MOD = 10**9 + 7
        count = 0
        length = 1  # Initialize length of the first character

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                length += 1
            else:
                count += (length * (length + 1)) // 2  # Calculate the count for the previous homogeneous substring
                length = 1  # Reset length for the new character

        count += (length * (length + 1)) // 2  # Calculate count for the last homogeneous substring

        return count % MOD

# Test cases
solution = Solution()
print(solution.countHomogenous("abbcccaa"))  # Output: 13
print(solution.countHomogenous("xy"))       # Output: 2
print(solution.countHomogenous("zzzzz"))    # Output: 15


