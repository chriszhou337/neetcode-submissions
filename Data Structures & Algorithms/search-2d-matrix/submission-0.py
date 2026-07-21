class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if target >= matrix[i][0] and target <= matrix[i][len(matrix[i]) - 1]:
                return self.binarySearch(matrix[i], target)
        
        return False

    def binarySearch(self, row: List[int], target: int) -> bool:
        L = 0
        R = len(row) - 1

        while L <= R:
            mid = (L + R) // 2

            if row[mid] == target:
                return True
            elif target < row[mid]:
                R = mid - 1
            elif target > row[mid]:
                L = mid + 1

        return False

