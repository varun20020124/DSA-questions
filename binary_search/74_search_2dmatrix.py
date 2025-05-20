class Solution:
    def searchMatrix(self, matrix, target):
        top = 0 
        bottom = len(matrix)-1
        row = -1
        while top<=bottom:
            mid = (top+bottom)//2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                row = mid
                break
            elif matrix[mid][-1] < target:
                top = mid + 1
            else:
                bottom = mid - 1
        low, high = 0, len(matrix[0])-1
        while low<=high:
            mid = (low+high)//2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return False