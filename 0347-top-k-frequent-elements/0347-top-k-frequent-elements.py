class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cntr = Counter(nums)
        ans = []
        for i in range(k):
            ans.append(cntr.most_common(k)[i][0])
        return ans