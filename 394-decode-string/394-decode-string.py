class Solution:
    
    def find_bracket(self, s:str) -> tuple:
        bracket = 0
        flag = False
        
        for i, ch in enumerate(s):
            
            if ch=="]":
                bracket -= 1
            if ch=="[":
                bracket += 1
                flag = True
            if bracket == 0:
                return flag, i
            
    
    def decodeString(self, s: str) -> str:
        k = ""
        word = ""
        sz, i = len(s), 0
        
        while(i<sz):
            ch = s[i]  
            
            if ch.isdigit():
                k += ch
            elif ch=="[":
                repetition = int(k)
                flag, end_idx = self.find_bracket(s[i:])
                end_idx += i
                if flag:
                    word += repetition * self.decodeString(s[i+1 : end_idx])
                else: 
                    word += repetition * s[i+1: end_idx]
                k = ""
                i = end_idx
            else:
                word += ch
                
            i += 1
                
                
            
        return word
        
        