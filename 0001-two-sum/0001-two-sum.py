class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if target == (nums[i]+nums[j]):
                    ans.append(i)
                    ans.append(j)
                    break
        return ans
