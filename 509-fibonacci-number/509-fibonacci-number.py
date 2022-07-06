class Solution:
    def fib(self, n: int) -> int:
        fib0 = 0
        fib1 = 1
        
        if n < 1:
            return fib0
        else:
            while(n>1):
                n -= 1
                fib0, fib1 = fib1, fib1+fib0
        return fib1
                
        