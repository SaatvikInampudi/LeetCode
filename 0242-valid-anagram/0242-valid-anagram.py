class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash1 = {}
        for i in s:
            hash1[i] = hash1.get(i,0)+1
        hash2 = {}
        for i in t:
            hash2[i] = hash2.get(i,0)+1
        if hash1 == hash2:
            return True
        return False