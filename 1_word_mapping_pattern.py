# word pattern 
"""
- Each letter in pattern maps to exactly one unique word in s.
- Each unique word in s maps to exactly one letter in pattern.
- No two letters map to the same word, and no two words map to the same letter

Input: pattern = "abba", s = "dog cat cat dog"
Output: true

The bijection can be established as:

'a' maps to "dog".
'b' maps to "cat".
"""
def wordPattern(pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """

        words = s.split()
        # First check, if they directly do not match lens = False
        if len(pattern) != len(words):
            return False

        # Create a empty dictionary to create the mappings
        d = {}
        for i in range(len(pattern)):
            # In case that we dont have the pattern mapped 
            if pattern[i] not in d:
                # in case that the word is already mapped, then we return false
                if words[i] in d.values():
                    return False
                # if not we map the pattern with the word
                d[pattern[i]] = words[i]
            else:
                # If we already have the pattern in the dictionary, 
                #we check if the word mapped in that index is equal to the word in that moment i
                # in case that they are not equal, we return false
                if d[pattern[i]] != words[i]:
                    return False
            print(d)
        return True

pattern = "abba" 
s = "dog cat cat fish"

wordPattern(pattern, s)