class Solution:
    def convert(self, s: str, Rows: int) -> str:
        #seq = Rows + (Rows - 2)   
        ans = ""
        up = True
        row = 0
        zig = [[] for x in range(Rows)]
        
        if Rows == 1:
            return s
        
        #Primeira Linha
        #for j, val in enumerate(s):
        #    if j % seq == 0:
        #        ans += val            
        #Linhas intermediarias
        #for i in range(1,Rows-1):
        #    for j, val in enumerate(s):
        #        if (j%seq == i) or (j%seq == seq-i):
        #            ans += val
        #Ultima Linha
        #for j, val in enumerate(s):
        #    if j%seq == seq/2:
        #        ans += val
    
        for val in s:
            zig[row].append(val)
            if up:
                if row < Rows-1:
                    row += 1
                else:
                    up, row = False, row-1
            else:
                if row > 0:
                    row -= 1
                else:
                    up, row = True, row+1
                    
        for linha in zig:
            for chrt in linha:
                ans += chrt
                
        return ans
        
            
        
        