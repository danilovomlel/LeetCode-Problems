class Solution:
    
    def Isom(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        letras = []
        trans = []
        
        for i, lt in enumerate(s):
            if not(lt in letras):
                letras.append(lt)
                trans.append(t[i])
            else:
                idx = letras.index(lt)
                if t[i] == trans[idx]:
                    pass
                else:
                    return False
        return True
        
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        return self.Isom(s,t) and self.Isom(t,s)
        
        