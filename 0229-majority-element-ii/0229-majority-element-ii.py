class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # c = Counter(nums)
        ans = []
        for i in range(len(Counter(nums).most_common(len(nums)))):
            if Counter(nums).most_common(len(nums))[i][1] > math.floor(len(nums)/3):
                ans.append(Counter(nums).most_common(len(nums))[i][0])
        return ans