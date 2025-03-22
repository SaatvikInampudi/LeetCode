class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # myset = set(nums)
        # ans = []
        # for i in range(1,len(nums)+1):
        #     if i not in myset:
        #         ans.append(i)
        # return ans

        # for i in range(1,len(nums)+1):
        #     if i
        return list(set(i for i in range(1,len(nums)+1)).difference(set(nums)))