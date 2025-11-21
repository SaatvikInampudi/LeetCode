class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c1 = Counter(s)
        c2 = Counter(t)

        if c1.items() == c2.items():
            return True
        return False
