class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:  # If there's only one element, no jump needed
            return 0
        
        jumps = 0  # Initialize jumps counter
        max_reachable = 0  # Initialize the maximum reachable index
        current_end = 0  # Initialize the current end index
        
        for i in range(n - 1):  # Iterate through the array except the last element
            max_reachable = max(max_reachable, i + nums[i])  # Update the maximum reachable index
            
            if i == current_end:  # If we reached the current end, it's time to make a jump
                jumps += 1  # Increment jump count
                current_end = max_reachable  # Update the current end to the new maximum reachable index
        
        return jumps
