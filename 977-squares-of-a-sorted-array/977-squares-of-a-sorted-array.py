class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        pow2 = lambda x: x**2
        nums = list(map(pow2, nums))
        nums.sort()
        return nums
        
        