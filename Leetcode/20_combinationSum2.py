class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()  # Sort the candidates to handle duplicates properly
        result = []
        self.backtrack(candidates, target, 0, [], result)
        return result
    
    def backtrack(self, candidates, target, start, path, result):
        if target == 0:
            result.append(path)
            return
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue  # Skip duplicates
            if candidates[i] > target:
                break  # Stop if candidate is greater than target
            self.backtrack(candidates, target - candidates[i], i + 1, path + [candidates[i]], result)

# Example usage:
candidates1 = [10, 1, 2, 7, 6, 1, 5]
target1 = 8
sol = Solution()
print(sol.combinationSum2(candidates1, target1))  # Output: [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]

candidates2 = [2, 5, 2, 1, 2]
target2 = 5
print(sol.combinationSum2(candidates2, target2))  # Output: [[1, 2, 2], [5]]
