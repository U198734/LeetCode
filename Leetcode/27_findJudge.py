class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        # Create arrays to count trust relationships
        trust_counts = [0] * (n + 1)
        trusted_by_counts = [0] * (n + 1)

        # Iterate through trust relationships
        for a, b in trust:
            trust_counts[a] += 1
            trusted_by_counts[b] += 1

        # Find the town judge
        for i in range(1, n + 1):
            if trust_counts[i] == 0 and trusted_by_counts[i] == n - 1:
                return i

        return -1
