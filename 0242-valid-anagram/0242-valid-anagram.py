class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {}
        dict_t = {}

        for char in s:  # Iterate over the original string, not the set
            dict_s[char] = dict_s.get(char, 0) + 1  # Increment count for each character
        
        for char in t:
            dict_t[char] = dict_t.get(char,0) + 1

        return dict_s == dict_t