'''
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 

Constraints:

1 <= nums.length <= 8
-10 <= nums[i] <= 10
'''
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(remaining, path):
            if not remaining:
                permutations.append(path[:])  # Append a copy of the path
                return
            
            visited = set()  # Track visited elements in this recursion level
            for i in range(len(remaining)):
                if remaining[i] not in visited:
                    visited.add(remaining[i])  # Mark the element as visited
                    backtrack(remaining[:i] + remaining[i+1:], path + [remaining[i]])
        
        permutations = []
        backtrack(nums, [])
        return permutations
