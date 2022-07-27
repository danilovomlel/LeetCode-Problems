class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words.sort()
        freq = defaultdict(int)
        ans = []
        
        for word in words:
            freq[word] += 1
            
        for i in range(k):
            word = max(freq, key=freq.get)
            ans.append(word)
            freq[word] = 0
            
        return ans
        