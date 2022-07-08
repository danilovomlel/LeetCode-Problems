class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        ans = []
        start, end = 0, -9999   
        
        while(key in nums):
            j = nums.index(key)
            nums[j] = float('inf')
            
            start = (j-k) if ((j-k) > (end-1)) else end
            start = start if start >= 0 else 0                
            end = j+k+1 if (j+k)<len(nums) else len(nums)
            
            print(start, end)
            for i in range(start, end):
                ans.append(i)
        
        return ans