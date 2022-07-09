class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        nums.sort()        
        for i, val in enumerate(nums[:len(nums)-1]):
            if val==nums[i+1]:
                return True
        return False
        