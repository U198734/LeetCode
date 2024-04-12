'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

'''
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Step 1: Convert to lowercase
        s = s.lower()
        
        # Step 2: Remove non-alphanumeric characters
        cleaned_s = ''.join(char for char in s if char.isalnum())
        
        # Step 3: Check if it's a palindrome
        return cleaned_s == cleaned_s[::-1]
