class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        
        # Iterate through characters of the first string
        for i, char in enumerate(strs[0]):
            # Iterate through other strings
            for string in strs[1:]:
                # Check if the current character matches
                if i >= len(string) or string[i] != char:
                    return strs[0][:i]  # Return the prefix found so far
        return strs[0]  # If all strings match, return the first string itself as the prefix
