class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # ans = []
        # for i in range(len(nums)):
        #     if nums[i] != 0:
        #         ans.append((math.prod(nums))//nums[i])
        #     else:
        #         nums[i], temp = 1, nums[i]
        #         ans.append(math.prod(nums))
        #         nums[i] = temp
        # return ans

        prefix = [1 for i in range(len(nums))]
        prefix[0] = nums[0]
        suffix = [1 for i in range(len(nums))]
        suffix[len(nums)-1] = nums[len(nums)-1]
        for i in range(1,len(nums)):
            prefix[i] = prefix[i-1]*nums[i]

        for j in range(len(nums)-2,-1,-1):
            suffix[j] = suffix[j+1]*nums[j]
        
        ans= [1 for i in range(len(nums))]
        # print(ans)
        ans[0] = suffix[1]
        ans[len(nums)-1] = prefix[len(nums)-2]
        for i in range(1,len(nums)-1):
            ans[i] = prefix[i-1]*suffix[i+1]
            # print(ans)
        return ans

        # n = len(nums)
        # ans = [1] * n  # Initialize answer array with 1

        # # Compute prefix products in ans array
        # prefix = 1
        # for i in range(n):
        #     ans[i] = prefix
        #     prefix *= nums[i]

        # # Compute suffix products directly in ans array
        # suffix = 1
        # for i in range(n-1, -1, -1):
        #     ans[i] *= suffix
        #     suffix *= nums[i]

        # return ans