class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        sz = len(nums)
        if sz == 1:
            if target > nums[0]:
                return 1
            else:
                return 0
        
        hf_sz = int(sz/2)
        L, R = nums[:hf_sz], nums[hf_sz:]
        
        if R and target == R[0]:
            return hf_sz
        elif L and target == L[-1]:
            return hf_sz-1
        elif L and R and target>L[-1] and target<R[0]:
            return hf_sz
        
        if R and target >=  R[0]:
            return hf_sz + self.searchInsert(R, target)
        elif L and target <= L[-1]:
            return self.searchInsert(L, target)
        
        
        