class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        #for i in range(k):
        #    num = nums.pop()
        #    nums.insert(0,num)
        
        sz = len(nums)
        if k>sz:
            k = k%sz
        nums[:] = nums[sz-k:] + nums[:sz-k]