class Solution:
    
    def search(self, nums: List[int], x: int) -> int:
        
        for i, val in enumerate(nums):
            if val >= x:
                return i
        return len(nums)
    
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        sz = len(stones)
        
        while(sz>1):
            bigger = stones.pop()
            big = stones.pop()
            
            if bigger == big:
                sz-= 2
            else:
                sz-= 1
                index = self.search(stones,bigger-big)
                stones.insert(index,bigger-big)
        
        if sz == 1:
            ans = stones[0]
        else:
            ans = 0
        
        return ans
        
        