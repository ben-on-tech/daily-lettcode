class Solution:
    def minTimeToVisitAllPoints(self, points: list[list[int]]) -> int:
        total_time = 0
        
        for i in range(len(points) - 1):
            
            x1 , y1 = points[i]
            x2, y2 = points[i + 1]
            
           
            total_time += max(abs(x1 - x2), abs(y1 - y2))
            
        return total_time
