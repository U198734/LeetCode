'''

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
'''

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(first=0):
            # If all integers are used up, add the current permutation to the result
            if first == n:
                result.append(nums[:])
            for i in range(first, n):
                # Place the current integer at the current index and recursively generate the rest of the permutations
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first + 1)
                # Backtrack: undo the previous swap
                nums[first], nums[i] = nums[i], nums[first]
        
        n = len(nums)
        result = []
        backtrack()
        return result

# Example usage:
solution = Solution()
print(solution.permute([1, 2, 3]))
print(solution.permute([0, 1]))
print(solution.permute([1]))










