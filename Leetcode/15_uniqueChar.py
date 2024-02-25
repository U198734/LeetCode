class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Create a dictionary to store character frequencies
        char_freq = {}
        
        # Populate the dictionary with character frequencies
        for char in s:
            char_freq[char] = char_freq.get(char, 0) + 1
        
        # Iterate through the string to find the first character with frequency 1
        for i in range(len(s)):
            if char_freq[s[i]] == 1:
                return i
        
        # If no unique character is found, return -1
        return -1
