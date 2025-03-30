class Solution:
    def search(self, nums: List[int], target: int) -> int:
        minelem = 0
        if nums[-1] > nums[0]:
            minelem = nums[0]
            min_index = 0
        l,r = 0, len(nums)-1
        minelem = nums[r]
        min_index = r
        while(l!=r):
            mid = (r+l)//2
            if minelem > nums[mid]:
                min_index = mid
            minelem = min(minelem,nums[mid])
            if nums[mid] > nums[r]:
                l = mid+1
            if nums[mid] <= nums[r]:
                r = mid
        
        if target == nums[-1]:
            return len(nums)-1
        elif target < nums[-1]:
            l = min_index
            r = len(nums)-1
        elif target > nums[-1]:
            l = 0
            r = min_index-1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1