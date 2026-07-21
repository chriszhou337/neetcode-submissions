class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])

        left = 0
        right = len(matrix) - 1

        row = 0

        while left <= right:
            median = (left + right) // 2
            print(matrix[median])

            if matrix[median][0] == target:
                return True
            elif matrix[median][0] < target and target <= matrix[median][m - 1]:
                row = median
                break
            elif matrix[median][0] < target and target > matrix[median][m - 1]:
                left = median + 1
            else:
                right = median - 1

        designatedRow = matrix[row]

        print(designatedRow)

        left = 0
        right = len(designatedRow) - 1

        while left <= right:
            median = (left + right) // 2

            if designatedRow[median] == target:
                return True
            elif designatedRow[median] < target:
                left = median + 1
            else:
                right = median - 1


        return False

        
            