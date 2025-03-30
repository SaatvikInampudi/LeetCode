class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Recursive helper function with an offset parameter
        def helper(arr, offset):
            if not arr:
                return -1  # base case: empty array, not found
            
            mid = len(arr) // 2
            if arr[mid] == target:
                return offset + mid  # return index adjusted by the offset
            
            # Search in the left half if target is less than the middle element
            elif target < arr[mid]:
                return helper(arr[:mid], offset)
            
            # Search in the right half if target is greater than the middle element
            else:
                return helper(arr[mid+1:], offset + mid + 1)
        
        return helper(nums, 0)



        # left, right = 0, len(nums) - 1
        # while left <= right:
        #     mid = (left + right) // 2
        #     if nums[mid] == target:
        #         return mid
        #     elif nums[mid] < target:
        #         left = mid + 1
        #     else:
        #         right = mid - 1
        # return -1