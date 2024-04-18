'''
Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...
 

Example 1:

Input: columnNumber = 1
Output: "A"
Example 2:

Input: columnNumber = 28
Output: "AB"
Example 3:

Input: columnNumber = 701
Output: "ZY"

'''


class Solution(object):
    def convertToTitle(self, columnNumber):
        result = ""
        while columnNumber > 0:
            columnNumber -= 1  # Adjust for 1-indexed columns
            char = chr((columnNumber % 26) + ord('A'))  # Convert remainder to character
            result = char + result
            columnNumber //= 26  # Integer division to get quotient
        return result
