class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans, idx = '', 0
        min_wrd = min(strs, key=len)
        flag = True
        
        while (idx < len(min_wrd) and flag):
            for i, wrds in enumerate(strs):
                if wrds[idx] == min_wrd[idx] and i+1==len(strs):
                    ans += min_wrd[idx]
                elif wrds[idx] == min_wrd[idx]:
                    pass
                else:
                    flag = False
                    break
            idx += 1            
        return ans
        