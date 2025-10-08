class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashm = {}
        for i in range(len(nums)):
            hashm[nums[i]] = i
        
        for i in range(len(nums)):
            if target-nums[i] in hashm:
                if target-nums[i] == nums[i] and hashm[target-nums[i]] == i:
                    continue
                return [i,hashm[target-nums[i]]]