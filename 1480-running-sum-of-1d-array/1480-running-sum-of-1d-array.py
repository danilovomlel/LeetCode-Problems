class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        try:
            ans=self.ans
        except AttributeError:
            self.ans = []
            ans = self.ans
            
        if len(nums)==1:
            ans.append(nums[0]+ans[-1]) if ans else ans.append(nums[0])
        else:
            ans.append(nums[0]+ans[-1]) if ans else ans.append(nums[0])
            self.runningSum(nums[1:])
        
        return self.ans