class Solution:
       
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 2:
            return min(cost)
        [n1, n2, result] = [0, 0, 0]
        for i in range(2, len(cost)+1):
            result = min(n1+cost[i-2], n2+cost[i-1])
            n1 = n2
            n2 = result
            
        return result