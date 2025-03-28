class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)-1):
            # if target == (numbers[i]+numbers[i+1]):
            #     return [i+1,i+2]
            
            left, right = i+1, len(numbers) - 1
            rem = target - numbers[i]
            while left <= right and rem>=numbers[i]:
                mid = (left + right) // 2
                
                if numbers[mid] == rem:
                    return [i+1,mid+1]
                elif numbers[mid] < rem:
                    left = mid + 1
                else:
                    right = mid - 1