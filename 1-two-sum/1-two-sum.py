class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        
        for i, value in enumerate(nums): 
            for j in range(i+1, len(nums)):
                if (value + nums[j]) == target:
                    ans.append(i)
                    ans.append(j)
                    break
            if len(ans)!=0:
                break
        return ans
                    