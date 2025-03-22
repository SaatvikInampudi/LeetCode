class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # d = {}
        # n = len(nums)
        # for i in range(n):
        #     rem = target - nums[i]
        #     if rem not in d:
        #         d[nums[i]] = i
        #     else:
        #         if i<d[rem]:
        #             return [i, d[rem]]
        #         else:
        #             return [d[rem], i]

        d = {}
        for i in range(len(nums)):
            d[nums[i]] = i
        
        for i in range(len(nums)):
            if (target-nums[i]) in d and d[target-nums[i]] != i:
                return [i,d[target-nums[i]]]








