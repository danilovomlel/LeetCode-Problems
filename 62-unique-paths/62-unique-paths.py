class Solution:
    def fact(self, n: int, div=0) -> int:
        if n==div:
            return 1
        else:
            return n*self.fact(n-1, div)
        
    def uniquePaths(self, m: int, n: int) -> int:
        if m>n:
            aux = n
            n = m
            m = aux
        C = m+n-2
        return int( self.fact(C,div=n-1)/ self.fact(m-1))
        