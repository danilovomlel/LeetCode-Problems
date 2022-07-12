class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        
        dist = [99999 for i in range(len(points))]
        
        for i, point in enumerate(points):
            
            if point[0] == x or point[1] == y:
                dist[i] = abs(x - point[0]) + abs(y - point[1])
        
        min_dist = min(dist)
        if min_dist<99999:
            return dist.index(min_dist)
        else:
            return -1
                