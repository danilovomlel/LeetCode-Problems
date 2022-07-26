class Solution:
    
    def erase_island(self, grid: List[List[str]], row: int, col: int):
        
        grid[row][col] = "0"
        steps = [ [0,1], [0,-1], [1,0], [-1,0] ]
        rows = len(grid)
        cols = len(grid[0])
        
        for step in steps:
            new_row = row + step[0]
            new_col = col + step[1]
            if rows>new_row>=0:
                if cols>new_col>=0:
                    if grid[new_row][new_col] == "1":
                        self.erase_island(grid, new_row, new_col)
            
            
        
    def numIslands(self, grid: List[List[str]]) -> int:
        
        islands = 0
        for i, row in enumerate(grid):
            for j, value in enumerate(row):
                if value=="1":
                    islands+=1
                    self.erase_island(grid, i, j)
                    
        return islands
        
        