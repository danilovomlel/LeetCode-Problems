class Solution:
    def counter(self, s: str) -> dict:
        ans = {}
        
        for ch in s:
            if ch in ans.keys():
                ans[ch] += 1
            else:
                ans[ch] = 1
        
        return ans
    
    def longestPalindrome(self, s: str) -> int:
        
        dict_count = self.counter(s)
        soma = 0
        tem_um = 0
        
        for ch_count in dict_count.values():
            if ch_count % 2 == 0:
                soma += ch_count
            else:
                soma += ch_count - 1
                tem_um = 1
        
        return soma + tem_um