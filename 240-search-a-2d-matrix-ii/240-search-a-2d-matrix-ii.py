class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n= len(matrix), len(matrix[0])
        i, j= 0, 0         
        
        while True:
            if matrix[i][j] == target:
                return True
            elif i+1<m and matrix[i+1][j]<=target:
                i+= 1
            elif j+1<n and matrix[i][j+1]<=target:
                j+= 1
            elif j+1<n:
                j+= 1
                while(i>=0 and (matrix[i][j] > target) ):
                    if i>=0:
                        i-= 1
                    if i<0:
                        return False
            else:
                return False
                
        
                