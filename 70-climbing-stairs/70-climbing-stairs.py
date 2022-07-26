class Solution:
    
    def fact(self, n: int, div=0) -> int:
        if n==div:
            return 1
        else:
            return n*self.fact(n-1, div)
    
    def combinacao(self, n: int, e: int) -> int:
        e_comp = n-e
        
        if e_comp > e: 
            aux = e
            e = e_comp
            e_comp = aux
            
        combin = int( self.fact(n,div=e)/self.fact(e_comp) )
        return combin
        
    def climbStairs(self, n: int) -> int:
        
        soma = 0
        escolhe = 0
        
        while(n>=escolhe):
            soma += self.combinacao(n, escolhe)
            n-=1
            escolhe+=1
        
        return soma
        
        