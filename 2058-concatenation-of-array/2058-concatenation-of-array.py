class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(2*len(nums)):
            if i<len(nums):
                # print(i)
                # print(ans[i])
                ans.append(nums[i])
            else: ans.append(nums[i-len(nums)])
        return ans
        