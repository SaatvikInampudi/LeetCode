class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # ana = []
        # reached = []
        # for n in range(len(strs)):
        #     ans = []
        #     if n not in reached:
        #         ans.append(strs[n])
        #         reached.append(n)
        #         for i in range(n+1,len(strs)):
        #             if i not in reached:
        #                 if Counter(strs[n]) == Counter(strs[i]):
        #                     ans.append(strs[i])
        #                     reached.append(i)

        #         ana.append(ans)
        # return ana
            
        # print(Counter(strs[0]))
        # n = 0
        # chk = Counter(strs[n])
        # ans.append(strs[n])
        # strs.pop(n)

        # for i in strs:
        #     if Counter(strs[i]) == chk:
        #         ans.append(strs[i])
        #         strs.pop(i)
        
        # dicto = {}
        # for i in range(len(strs)):
        #     sort_wrd = ''.join(sorted(strs[i]))
        #     # sort_wrd = sorted(strs[i])
        #     print(sort_wrd)
        #     if sort_wrd in dicto:
        #         dicto[sort_wrd].append(strs[i])
        #     else:
        #         dicto[sort_wrd] = [strs[i]]
        # return list((dicto.values()))


        dicto = {}
        for word in strs:
            key = frozenset(Counter(word).items())  # frozenset of (char, count) pairs
            print(key)
            if key in dicto:
                dicto[key].append(word)
            else:
                dicto[key] = [word]
        return list(dicto.values())