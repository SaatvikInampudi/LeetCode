class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i in range(len(nums)):
            hm[nums[i]] = i
        print(hm)
        for i in range(len(nums)):
            if target-nums[i] in hm:
                if hm[target-nums[i]] == hm[nums[i]] and hm[target-nums[i]]==i:
                    continue
                return [hm[target-nums[i]],i]

