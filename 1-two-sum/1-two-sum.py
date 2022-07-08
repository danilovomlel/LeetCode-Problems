class Solution:
    def twoSum(self, nums: List[int], k: int) -> List[int]:
        ans = []
        trgt= j= 0
        
        for i, value in enumerate(nums):
            trgt = k - value
            if trgt in nums[i+1:]:
                j = nums[i+1:].index(trgt)
                ans.append(i)
                ans.append(j+i+1)
                break
        return ans
                    