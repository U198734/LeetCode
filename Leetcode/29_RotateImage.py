class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        
        # Rotate layer by layer
        for layer in range(n // 2):
            first = layer
            last = n - 1 - layer
            for i in range(first, last):
                offset = i - first
                # Save top
                top = matrix[first][i]
                # left -> top
                matrix[first][i] = matrix[last - offset][first]
                # bottom -> left
                matrix[last - offset][first] = matrix[last][last - offset]
                # right -> bottom
                matrix[last][last - offset] = matrix[i][last]
                # top -> right
                matrix[i][last] = top
