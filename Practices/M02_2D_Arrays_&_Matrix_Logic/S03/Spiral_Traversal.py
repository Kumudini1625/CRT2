'''from typing import List
def spiralOrder(matrix: List[List[int]]) -> List[int]:
    rows, cols = len(matrix), len(matrix[0])
    top, bottom = 0, rows - 1
    left, right = 0, cols - 1
    res = []

    while top <= bottom and left <= right:

        # Top row
        for c in range(left, right + 1):
            res.append(matrix[top][c])
        top += 1

        # Right column
        for r in range(top, bottom + 1):
            res.append(matrix[r][right])
        right -= 1

        # Bottom row
        if top <= bottom:
            for c in range(right, left - 1, -1):
                res.append(matrix[bottom][c])
            bottom -= 1

        # Left column
        if left <= right:
            for r in range(bottom, top - 1, -1):
                res.append(matrix[r][left])
            left += 1

    return res
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(spiralOrder(matrix))
'''


from typing import List
def generateMatrix(n: int) -> list[list[int]]:
        res= [[0] * n for _ in range(n)]

        top, bottom = 0, n - 1
        left, right = 0, n - 1
        num = 1

        while top <= bottom and left <= right:

            # Left -> Right
            for col in range(left, right + 1):
                res[top][col] = num
                num += 1
            top += 1

            # Top -> Bottom
            for row in range(top, bottom + 1):
                res[row][right] = num
                num += 1
            right -= 1

            # Right -> Left
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    res[bottom][col] = num
                    num += 1
                bottom -= 1

            # Bottom -> Top
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    res[row][left] = num
                    num += 1
                left += 1

        return res
n = 3
print(generateMatrix(n))


