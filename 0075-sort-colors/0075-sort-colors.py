# import heapq
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # # heapq.heapify(nums)
        # # print(Counter(nums).get(0))
        # # nums = [0 for i in range(Counter(nums).get(0))]
        
        counter = Counter(nums)
        x = counter.get(0, 0)
        y = counter.get(1, 0)
        z = counter.get(2, 0)

        # Modify nums in-place
        index = 0
        for _ in range(x):
            nums[index] = 0
            index += 1
        for _ in range(y):
            nums[index] = 1
            index += 1
        for _ in range(z):
            nums[index] = 2
            index += 1
