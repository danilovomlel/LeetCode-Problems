class Solution:
    def convert(self, s: str, Rows: int) -> str:
        seq = Rows + (Rows - 2)   
        ans = ""
        
        if Rows == 1:
            return s
        else:
            #Primeira Linha
            for j, val in enumerate(s):
                if j % seq == 0:
                    ans += val            
            #Linhas intermediarias
            for i in range(1,Rows-1):
                for j, val in enumerate(s):
                    if (j%seq == i) or (j%seq == seq-i):
                        ans += val
            #Ultima Linha
            for j, val in enumerate(s):
                if j%seq == seq/2:
                    ans += val
                
        return ans
        
            
        
        