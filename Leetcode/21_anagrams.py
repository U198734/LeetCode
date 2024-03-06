class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams = {}
        
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in anagrams:
                anagrams[sorted_word] = [word]
            else:
                anagrams[sorted_word].append(word)
        
        return list(anagrams.values())

# Example usage:
strs1 = ["eat","tea","tan","ate","nat","bat"]
strs2 = [""]
strs3 = ["a"]

solution = Solution()
print(solution.groupAnagrams(strs1))  # Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
print(solution.groupAnagrams(strs2))  # Output: [[""]]
print(solution.groupAnagrams(strs3))  # Output: [["a"]]
