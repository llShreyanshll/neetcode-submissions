class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        inner_l, inner_r = 0, len(matrix[0]) - 1

        while l <= r:
            m = (l + r) // 2

            if target > matrix[m][inner_r]:
                l = m + 1
            elif target < matrix[m][inner_l]:
                r = m - 1
            else:
                break

        while inner_l <= inner_r:
            inner_m = (inner_l + inner_r) // 2

            if target > matrix[m][inner_m]:
                inner_l = inner_m + 1
            elif target < matrix[m][inner_m]:
                inner_r = inner_m - 1
            else:
                return True

        return False
            

        