class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        
        if len(s1) != len(s2):
            return False
        if s1==s2:
            return True
        idx1, idx2 = -1, -1
        
        for i, ch, in enumerate(s1):
            if ch==s2[i]:
                pass
            elif idx1<0:
                idx1 = i
            elif idx2<0:
                idx2 = i
            else:
                return False
        
        if (idx1>-1) and (idx2>-1):
            if s1[idx1]==s2[idx2] and s2[idx1]==s1[idx2]:
                return True
        return False