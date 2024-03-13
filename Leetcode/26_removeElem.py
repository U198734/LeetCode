class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # Initialize a pointer to keep track of the position for non-val elements
        k = 0
        
        # Iterate through the array
        for i in range(len(nums)):
            # If the current element is not equal to val, move it to the position pointed by k
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        
        # The value of k is the number of elements in nums which are not equal to val
        return k