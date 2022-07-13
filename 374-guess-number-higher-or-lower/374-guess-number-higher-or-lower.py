# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        hf= int(n/2) if int(n/2)>=1 else 1
        soma= hf
        compare= guess(hf)
        while(compare!=0):
            
            if compare == 1:
                compare = guess(soma + hf)
                soma+= hf
            elif compare == -1:
                compare = guess(soma - hf)
                soma-= hf
            
            hf = int(hf/2) if int(hf/2)>=1 else 1
        
        
        
        
        
        return soma
        