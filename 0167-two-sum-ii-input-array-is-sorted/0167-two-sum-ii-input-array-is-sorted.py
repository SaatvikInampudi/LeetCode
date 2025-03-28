class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # for i in range(len(numbers)-1):
            # if target == (numbers[i]+numbers[i+1]):
            #     return [i+1,i+2]
            
        left, right = 0, len(numbers) - 1
        # rem = target - numbers[i]
        while left < right:
            # mid = (left + right) // 2
            
            if numbers[left]+numbers[right] == target:
                return [left+1,right+1]
            elif numbers[left]+numbers[right] < target:
                left += 1
            else:
                right -= 1