class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # for i in range(len(strs)):
        #     for k in range(i+1,len(strs)):
        #         if len(strs[i])<=len(strs[k]):
        #             for j in range(1,len(strs[k])):
        #                 if (strs[i][:j] == strs[k][:j]):
        #                     ans = strs[i][:j]
        #                 else:
        #                     ans = ""
        #         else:
        #             for j in range(1,len(strs[i])):
        #                 if strs[i][:j] == strs[k][:j]:
        #                     ans = strs[i][:j]
        #                 else:
        #                     ans = ""
        print(len(strs))
        if len(strs) > 1 :  
            check = 0
            # max_len = 0
            # for x in range(len(strs)):
            #     if len(strs[x]) > max_len:
            #         max_len = len(strs[x])

            lcp = strs[0][:1]
            # print('max=',max_len)
            print(lcp)
            if len(strs[0]) != 0:
                print('chk')
                for j in range(1,len(strs[0])+1):
                    print('j',j)
                    for i in range(1,len(strs)):
                        print('i',i)
                        print(strs[i][:j])
                        if (strs[i][:j] == lcp):
                            print('chk2')
                            if i == len(strs)-1 and j == len(strs[0]):
                                return lcp
                            continue
                        else:
                            print('check')
                            check = 1
                            if len(lcp[:len(lcp)-1]) != 0:
                                print('testing',len(lcp[:len(lcp)-1]))
                                return lcp[:len(lcp)-1]
                            else:
                                return ""
                            break
                    print('before incr=',lcp)
                    lcp = strs[0][:j+1]
                    print('after incrementing lcp=',lcp)
                    if check == 1:
                        break
            else:
                return ""
        else:
            print('test')
            return strs[0]
