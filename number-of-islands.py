class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid: return 0
        
        islands = 0
        
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                if grid[i][j] == "1":
                    islands += 1
                    
                    self.sink(grid, i, j)
                    
        return islands

    def sink(self, grid, i, j):
        
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == "0":
            return
        
       
        grid[i][j] = "0"
        
        
        self.sink(grid, i + 1, j) 
        self.sink(grid, i - 1, j) 
        self.sink(grid, i, j + 1) 
        self.sink(grid, i, j - 1)
