class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # Base case: If exponent is 0, return 1
        if n == 0:
            return 1
        
        # Handling negative exponent
        if n < 0:
            x = 1 / x
            n = -n
        
        # Recursive computation
        half = self.myPow(x, n // 2)
        
        # If exponent is even
        if n % 2 == 0:
            return half * half
        # If exponent is odd
        else:
            return x * half * half