class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        j = 0
        ans = 0
        dif = 0
        
        for i, val in enumerate(nums):
            j=i+1
            while(j<len(nums)):
                val2 = nums[j]
                dif = val-val2 if val > val2 else val2-val 
                ans = ans+1 if dif==k else ans
                j+= 1
        return ans
        
        