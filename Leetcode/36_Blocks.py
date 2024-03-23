class Solution(object):
    def bagOfTokensScore(self, tokens, power):
        tokens.sort()  # Sort tokens to facilitate the greedy strategy
        max_score = 0
        score = 0
        left = 0
        right = len(tokens) - 1
        
        while left <= right:
            if power >= tokens[left]:  # If we can play the token face-up
                power -= tokens[left]
                score += 1
                left += 1
                max_score = max(max_score, score)
            elif score > 0:  # If we can play the token face-down
                power += tokens[right]
                score -= 1
                right -= 1
            else:
                break
                
        return max_score

# Example usage:
solution = Solution()
print(solution.bagOfTokensScore([100], 50))  # Output: 0
print(solution.bagOfTokensScore([200, 100], 150))  # Output: 1
print(solution.bagOfTokensScore([100, 200, 300, 400], 200))  # Output: 2
