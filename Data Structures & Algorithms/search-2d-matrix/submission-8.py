class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        line_left, line_right = 0, len(matrix) - 1
        middle_line = 0

        while line_left <= line_right:
            middle_line = (line_left + line_right) // 2

            if matrix[middle_line][0] <= target <= matrix[middle_line][-1]:
                break
            elif matrix[middle_line][-1] < target:
                line_left = middle_line + 1
            else:
                line_right = middle_line - 1

        col_left, col_right = 0, len(matrix[0]) - 1

        while col_left <= col_right:
            middle_col = (col_left + col_right) // 2
            
            if matrix[middle_line][middle_col] == target:
                return True
            elif matrix[middle_line][middle_col] < target:
                col_left = middle_col + 1
            else:
                col_right = middle_col - 1
        
        return False