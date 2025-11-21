class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        hashm = {}
        sortedlist = []
        for i in strs:
            key = "".join(sorted(i))
            sortedlist.append(key)

        for i in range(len(sortedlist)):
            # print(sortedlist[i])
            if sortedlist[i] in hashm:
                ans[hashm[sortedlist[i]]].append(strs[i])
            else:
                hashm[sortedlist[i]]= len(ans)
                ans.append([strs[i]])
        return ans
            


        # skip = set()

        # for i in range(len(strs)):
        #     if i in skip:
        #         continue
        #     subans = []
        #     subans.append(strs[i])
        #     skip.add(i)
        #     for j in range(i+1,len(strs)):
        #         if j in skip:
        #             continue
        #         if hashm[j] == hashm[i]:
        #             subans.append(strs[j])
        #             skip.add(j)
        #     ans.append(subans)
        # return ans
            