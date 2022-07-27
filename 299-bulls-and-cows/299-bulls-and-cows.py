class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        secret_map, guess_map = defaultdict(int), defaultdict(int) 
        
        for i, ch in enumerate(secret):
            secret_map[ch] += 1
            guess_map[guess[i]] += 1
            if ch == guess[i]:
                bulls += 1
        
        for key in secret_map.keys():
            if key in guess_map:
                cows += min(secret_map[key], guess_map[key])
        cows = cows - bulls
        ans = str(bulls) + "A" + str(cows) + "B"
        return ans
        