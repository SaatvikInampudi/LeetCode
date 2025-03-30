class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        freq = {}
        maxlen = 0
        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1
             
            cur_len = r - l + 1
            if cur_len - max(freq.values()) <= k:  
                maxlen = max(maxlen, cur_len)
            else:                               
                freq[s[l]] -= 1                 
                l += 1
               
        return maxlen