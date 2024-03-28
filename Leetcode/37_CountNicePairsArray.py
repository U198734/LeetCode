class Solution(object):
    def countNicePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        
        def rev(x):
            return int(str(x)[::-1])
        
        differences = {}
        for num in nums:
            diff = num - rev(num)
            differences[diff] = differences.get(diff, 0) + 1
        
        nice_pairs_count = 0
        for freq in differences.values():
            nice_pairs_count += freq * (freq - 1) // 2
        
        return nice_pairs_count % MOD
