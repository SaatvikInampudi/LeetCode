class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # to_rem = set()
        k = 0
        for i in range(len(nums)):
            if val != nums[i]:
                # to_rem.add(i)
                k+=1
        nums.sort(key = lambda x: x==val)
        # for i in to_rem:
        #     nums.pop(i)
        print(k)
        return k
                