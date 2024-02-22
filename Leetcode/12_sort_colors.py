class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # Initialize pointers for the three sections
        left, mid, right = 0, 0, len(nums) - 1
        
        # Traverse the array
        while mid <= right:
            if nums[mid] == 0:
                # If the current element is 0, swap with the element at the left pointer
                nums[left], nums[mid] = nums[mid], nums[left]
                left += 1
                mid += 1
            elif nums[mid] == 1:
                # If the current element is 1, move to the next element
                mid += 1
            else:
                # If the current element is 2, swap with the element at the right pointer
                nums[mid], nums[right] = nums[right], nums[mid]
                right -= 1
        
        # At the end, the array will be sorted
