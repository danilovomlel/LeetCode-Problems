class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()
        ch, cuk = 0, 0
        happy = 0
        
        while(cuk<len(s)):
            if ch<len(g) and s[cuk] >= g[ch]:
                ch, cuk= ch+1, cuk+1
                happy += 1
            else:
                cuk +=1
        return happy
        