class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        #SOL 1
        #try:
        #    ans=self.ans
        #except AttributeError:
        #    self.ans = []
        #    ans = self.ans
        #    
        #if len(nums)==1:
        #    ans.append(nums[0]+ans[-1]) if ans else ans.append(nums[0])
        #else:
        #    ans.append(nums[0]+ans[-1]) if ans else ans.append(nums[0])
        #    self.runningSum(nums[1:])
        #
        #return self.ans
        
        #SOL 2
        #ans=[]
        #for val in nums:
        #    ans.append(ans[-1]+val) if ans else ans.append(val)
        #return ans
        
        #SOL 3
        for i, val in enumerate(nums):
            nums[i] = nums[i]+nums[i-1] if i>0 else nums[i]
        return nums