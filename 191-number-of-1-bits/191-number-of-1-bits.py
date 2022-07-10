class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        BITS = 32
        pow2 = lambda x: (2*pow2(x-1)) if x>0 else 1
        Dois = pow2(BITS)*2
        
        for i in range(BITS-1,-1,-1):
            Dois = int(Dois/2)
            
            if n>=Dois:
                ans, n = ans+1, n-Dois
        
        return ans+n
        