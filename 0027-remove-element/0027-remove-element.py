class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if val != nums[i]:
                nums[k] = nums[i]
                k+=1
        # nums.sort(key = lambda x: x==val)
        print(k)
        return k
                