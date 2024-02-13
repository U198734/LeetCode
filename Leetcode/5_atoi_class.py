class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Initialize variables
        result = 0
        sign = 1
        i = 0
        n = len(s)

        # Ignore leading whitespace
        while i < n and s[i] == ' ':
            i += 1

        # Check for sign
        if i < n and (s[i] == '+' or s[i] == '-'):
            sign = -1 if s[i] == '-' else 1
            i += 1

        # Process digits
        while i < n and s[i].isdigit():
            digit = int(s[i])
            # Check for overflow
            if result > (2 ** 31 - 1) // 10 or (result == (2 ** 31 - 1) // 10 and digit > 7):
                return -2 ** 31 if sign == -1 else 2 ** 31 - 1
            result = result * 10 + digit
            i += 1

        return sign * result
