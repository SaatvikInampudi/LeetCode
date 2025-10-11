class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # print(type(strs[0][0]))
        pref = ""
        itr = ""
        minstr = len(strs[0])
        if len(strs) == 1:
            return strs[0]
        for i in range(1,len(strs)):
            # print(i,len(strs)-1)
            # print(minstr,"i=",i)
            # print(len(strs[i]),"i=",i)
            if len(strs[i])< minstr:
                minstr = len(strs[i]) 
        for j in range(minstr):
            # print(j)
            for i in range(1,len(strs)):
                # print(i,j,len(strs)-1)
                # print(strs[i][j],strs[i-1][j])
                if strs[i][j] == strs[i-1][j]:
                    itr = strs[i][j]
                    # print(i,j,itr)
                else:
                    # print(i,j,itr)
                    itr = ""
                    # print(i,j)
                    break
            # print(i,j,itr)
            if itr != "":
                pref += itr
            else: break
        return pref
                