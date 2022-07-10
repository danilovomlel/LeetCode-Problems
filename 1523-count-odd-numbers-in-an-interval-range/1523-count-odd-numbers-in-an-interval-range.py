class Solution:
    def countOdds(self, low: int, high: int) -> int:
        sz = high-low+1
        
        if sz%2==0:
            return int(sz/2)
        elif high%2==0:
            return int(sz/2)
        else:
            return int(1+sz/2)
        