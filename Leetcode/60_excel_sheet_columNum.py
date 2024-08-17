'''
A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
'''
# Observations
# 1 - 26 --> A - Z
# AA - AZ --> 27 - 53
# For example : 
# "ZY" --> (26**1 * 26) + (26**0 * 25) = 701
# "AAA" --> (26**2 * 26) + (26**1 * 26) + (26**0 * 1)
# So we can see a pattern that we can represent with a formula

# We can use ord(char) to obtain the value of the corresponding letter
def letters_to_number(s):
    result = 0
    for i, char in enumerate(reversed(s)):
        result += (ord(char) - ord('A') + 1) * (26 ** i)
    return result

print(letters_to_number("AAA"))  # Output: 701
