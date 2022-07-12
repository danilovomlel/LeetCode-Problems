class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
        nums.sort()
        idx = len(nums)-1
        large, idx = nums[idx], idx-1
        medium, idx = nums[idx], idx-1
        small = nums[idx]
        
        while(idx>=0):
            
            if large<medium+small:
                return large+medium+small
            else:
                idx-= 1
                large = medium
                medium = small
                small = nums[idx]              
        
        return 0