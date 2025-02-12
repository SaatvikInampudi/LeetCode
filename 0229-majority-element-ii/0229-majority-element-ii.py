class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        ans = []
        for i in range(len(c.most_common(len(nums)))):
            if c.most_common(len(nums))[i][1] > math.floor(len(nums)/3):
                ans.append(c.most_common(len(nums))[i][0])
        return ans