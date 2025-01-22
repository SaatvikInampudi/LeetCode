class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Check if lengths are the same; if not, they can't be anagrams
        if len(s) != len(t):
            return False
        
        # Sort both strings and compare them
        return sorted(s) == sorted(t)