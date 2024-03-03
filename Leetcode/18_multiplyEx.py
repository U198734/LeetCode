class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == "0" or num2 == "0":
            return "0"
        
        len1, len2 = len(num1), len(num2)
        result = [0] * (len1 + len2)
        
        for i in range(len1-1, -1, -1):
            for j in range(len2-1, -1, -1):
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                total = mul + result[i+j+1]
                result[i+j] += total // 10
                result[i+j+1] = total % 10
        
        # Remove leading zeros
        result_str = ''.join(map(str, result))
        return result_str.lstrip('0') or '0'