class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        res = []

        top, buttom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top <= buttom and left <= right:

            for col in range(left, right + 1):
                res.append(matrix[top][col])
            top += 1

            for row in range(top, buttom + 1):
                res.append(matrix[row][right])
            right -= 1

            if top <= buttom:
                for col in range(right, left - 1, -1):
                    res.append(matrix[buttom][col])
                buttom -= 1

            if left <= right:
                for row in range(buttom, top - 1, -1):
                    res.append(matrix[row][left])
                left += 1

        return res
