# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        FBV = int(n/2) + 1
        isBad = isBadVersion(FBV)
        last = n
        
        if isBadVersion(1):
            return 1
        
        while( not( isBad and not(isBadVersion(FBV-1)) ) ):
            print(FBV)
            if isBad:
                last = FBV
                FBV = FBV - int(last/2)
            
            else:
                if last - FBV == 1:
                    FBV = last
                else:
                    FBV = FBV + int((last-FBV)/2)
                
                
            isBad = isBadVersion(FBV)
        
        return FBV
        