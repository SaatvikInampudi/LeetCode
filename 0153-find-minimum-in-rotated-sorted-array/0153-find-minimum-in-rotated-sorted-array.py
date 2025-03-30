class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[-1] > nums[0]:
            return nums[0]
        l,r = 0, len(nums)-1
        minval = nums[r]
        while(l!=r):
            mid = (r+l)//2
            minval = min(minval,nums[mid])
            if nums[mid] > nums[r]:
                l = mid+1
            if nums[mid] <= nums[r]:
                r = mid
        return minval
            
