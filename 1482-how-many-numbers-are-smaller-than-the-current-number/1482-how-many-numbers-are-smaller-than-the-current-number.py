class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sortedlist = sorted(nums)
        d = {}
        for i in range(len(sortedlist)):
            if sortedlist[i] not in d:
                d[sortedlist[i]] = i
        
        ans = []

        for i in nums:
            ans.append(d[i])

        return ans
