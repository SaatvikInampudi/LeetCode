class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        check = {}
        for i in range(len(nums)):
            if nums[i] in check:
                # print(check)
                # print(nums[i])
                return True
            else:
                check[nums[i]] = 1
        # print(check)
        return False

        