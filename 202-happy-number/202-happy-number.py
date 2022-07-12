class Solution:
    
    def iterate(self, n):
        soma= 0
        while(n>=1):
            dig = n%10
            soma+= dig*dig
            n = int(n/10)
        return soma
    
    def underHundred(self, n):
        while(n>99):
            n= self.iterate(n)
        return n
            
    def isHappy(self, n: int) -> bool:
        Happy = [1,7,44,13,31,19,91,28,82,68,86,10,70,23,32,49,94,79,97]
        n = self.underHundred(n)
        
        if n in Happy:
            return True
        else:
            return False
        