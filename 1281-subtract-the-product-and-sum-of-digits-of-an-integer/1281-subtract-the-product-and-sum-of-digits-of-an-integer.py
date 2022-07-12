class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        dig = n%10
        soma=dig
        prod=dig
        n= int(n/10)
        while(n>=1):
            dig = n%10
            soma+=dig
            prod*=dig
            n= int(n/10)
        print(prod,soma)
        return prod-soma