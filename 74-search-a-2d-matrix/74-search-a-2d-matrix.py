class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        col = []
        [col.append(i[0]) for i in matrix]
        
        for i, val in enumerate(col):
            if target >= val:
                for val2 in matrix[i]:
                    if val2 == target:
                        return True
                    elif val2 > target:
                        break
            else:
                break
        return False
            
        