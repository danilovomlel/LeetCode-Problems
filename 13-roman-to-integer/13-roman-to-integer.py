class Solution:
    def romanToInt(self, s: str) -> int:
        soma = 0
        value = {'I': 1, 
                 'V': 5,
                 'X': 10,
                 'L': 50,
                 'C': 100,
                 'D': 500,
                 'M': 1000,
                }
        spy = 0
        
        for i, char in enumerate(s):
            if i < len(s)-1:
                spy = s[i+1]
                if value[spy] > value[char]:
                    soma -= value[char]
                else:
                    soma += value[char]
        soma += value[ s[len(s)-1] ]
                
            
        
        
        return soma
        
        
        