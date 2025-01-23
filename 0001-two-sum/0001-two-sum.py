class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        n = len(nums)
        for i in range(n):
            rem = target - nums[i]
            if rem not in d:
                d[nums[i]] = i
            else:
                return [i, d[rem]]
