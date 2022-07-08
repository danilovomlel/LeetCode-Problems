class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        ans = -1
        L = [0 for i in range(len(nums))] 
        R = [0 for i in range(len(nums))]
        
        for i in range(len(R)-1, -1, -1):
            R[i] = nums[i]+R[i+1] if i<len(nums)-1 else nums[i]
        
        for i in range(len(L)):
            L[i] = nums[i]+L[i-1] if i>0 else nums[i]
            
        for i in range(len(L)):
            if L[i]==R[i]:
                ans=i
                break                
        return ans
        
        