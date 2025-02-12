class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if nums==[]:
            return 0
        # count = 0
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)+1):
        #         # print(i,j,sum(nums[i:j]),count)
        #         if sum(nums[i:j]) == k:
        #             count+=1
        #             pass
        #         else: 
        #             pass
        # return count

        hashmap = {}
        anss = 0

        prefix_sum = 0
        # hashmap[nums[0]] = 1
        # prefix_sum[0] = nums[0]
        for num in nums:
            prefix_sum += num
            # print(prefix_sum)
            if prefix_sum-k in hashmap:
                # print('chk')
                anss += hashmap[prefix_sum-k]
            hashmap[prefix_sum] = hashmap.get(prefix_sum,0) + 1
            # print(hashmap)
            if prefix_sum == k:
                # print('chk2')
                anss += 1
        return anss

        # for i in prefix_sum:
        #     if i == k:
        #         cnt +=1
        #     if i != k or k ==0:
        #         if i-k in hashmap:
                    

        # print(prefix_sum)

        
        # print('1->',k, prefix_sum)
        # if k in prefix_sum:
        #     anss += prefix_sum.count(k)
        #     print('anss',anss)

        # for i in range(len(prefix_sum)):
        #     if prefix_sum[i] != k or k == 0:
        #         if (prefix_sum[i] - k) in prefix_sum[:i]:
        #             print((prefix_sum[i] - k))
        #             anss += prefix_sum[:i].count((prefix_sum[i] - k))
        # return anss

        # prefix_sum = []
        # for i in nums:
        #     prefix_sum.append

        # for i in prefix_sum:
        #     hashmap[i] = hashmap.get(i,0) + 1


        

