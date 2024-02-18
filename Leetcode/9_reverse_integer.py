class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Define the range limits
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        # Convert integer to string and handle the sign
        is_negative = x < 0
        str_x = str(abs(x))
        
        # Reverse the string
        reversed_str = str_x[::-1]
        
        # Convert back to integer and reapply the sign
        reversed_x = int(reversed_str) * (-1 if is_negative else 1)
        
        # Check if reversed_x is within the range [-2^31, 2^31 - 1]
        if reversed_x < INT_MIN or reversed_x > INT_MAX:
            return 0
        else:
            return reversed_x