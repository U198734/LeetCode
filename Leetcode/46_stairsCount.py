'''
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step


# n = 3
# (2 * 0 ) + 3
# (2 * 1)  + 1

# 2 1
# 1 2
# 1 1 1

# So --> 3 possibilities

# n = 4
# (2 * 0) + 4
# (2 * 1) + 2
# (2 * 2) + 0

# 2 2 
# 1 1 1 1
# 2 1 1
# 1 1 2 
# 1 2 1

# So --> 5 possibilities 
'''

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        
        prev_prev_step = 1
        prev_step = 2
        
        for _ in range(3, n + 1):
            current_step = prev_step + prev_prev_step
            prev_prev_step, prev_step = prev_step, current_step
        
        return prev_step