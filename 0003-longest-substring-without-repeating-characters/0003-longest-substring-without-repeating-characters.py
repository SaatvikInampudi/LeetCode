class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == '':
            return 0
        l=0
        maxstr = 0
        visi = {}

        for r in range(len(s)):
            # if s[r] in visi:
            if s[r] in visi and visi[s[r]] >= l:
                l = visi[s[r]] + 1
                visi[s[r]] = r
                # print('l',l)
                continue
            else:
                visi[s[r]] = r
                maxstr = max(maxstr,r-l+1)
                # print(visi)
                # print('max',maxstr)
        maxstr = max(maxstr,r-l+1)
        return maxstr
