class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        max_ans = 0
        substring = []
        i = 0
        j = 0
        
        while i < len(s):
            if s[i] in substring:
                max_ans = max(max_ans, ans)
                ans = 1
                
                j = i
                while True:
                    j -= 1
                    if s[i] == s[j]:
                        i = j+1
                        substring.clear()
                        substring.append(s[i])
                        break
                    
            else:
                substring.append(s[i])
                ans += 1
            i += 1

        max_ans = max(max_ans, ans)
        
        return max_ans
        