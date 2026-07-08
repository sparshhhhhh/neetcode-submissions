class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        top = 0
        bot = m-1
        while top<=bot:
            row = (top+bot)//2
            if target < matrix[row][0]:
                bot = row-1
            elif target > matrix[row][n-1]:
                top = row+1
            else:
                break
        l = 0
        r = n-1
        print(row)
        while l<=r:
            mid = l + (r-l)//2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                r = mid-1
            else:
                l = mid+1
        return False
                