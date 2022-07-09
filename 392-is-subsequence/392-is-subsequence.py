class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        if len(t)<len(s):
            return False
        if not(s):
            return True
        
        j=0
        for lt in t:
            if lt in s[j]:
                j = j+1
                if j == len(s):
                    return True
                
        return False
        
        