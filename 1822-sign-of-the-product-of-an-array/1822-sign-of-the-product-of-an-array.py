class Solution:
    def arraySign(self, nums: List[int]) -> int:
        negatives = 0
        for val in nums:
            if val<0:
                negatives+= 1
            elif val==0:
                return 0
        if negatives%2==0:
            return 1
        else:
            return -1
        