class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref = ""
        itr = ""
        minstr = len(strs[0])
        if len(strs) == 1:
            return strs[0]
        for i in range(1,len(strs)):
            if len(strs[i])< minstr:
                minstr = len(strs[i]) 
        for j in range(minstr):
            for i in range(1,len(strs)):
                if strs[i][j] == strs[i-1][j]:
                    itr = strs[i][j]
                else:
                    itr = ""
                    break
            if itr != "":
                pref += itr
            else: break
        return pref
                