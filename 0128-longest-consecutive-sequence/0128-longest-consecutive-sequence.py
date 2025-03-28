class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        # minheap = []
        # for i in nums:
        #     heapq.heappush(minheap, i)
        # sorted_list = [heapq.heappop(minheap) for _ in range(len(minheap))]
        # sorted_list = list(dict.fromkeys(sorted_list))
        # print(sorted_list)
        # ans = 1
        # max_ans = 0
        # for i in range(1,len(sorted_list)):
        #     if sorted_list[i] == sorted_list[i-1]+1:
        #         ans+=1
        #     else:
        #         if ans>max_ans:
        #             max_ans = ans
        #         ans = 1
        # if ans>max_ans:
        #         max_ans = ans
        # return max_ans


        # nums.sort()

        # ans = 1
        # max_ans = 0
        # for i in range(1,len(nums)):
        #     if nums[i] == nums[i-1]:
        #         pass
        #     else:
        #         if nums[i] == nums[i-1]+1:
        #             ans+=1
        #         else:
        #             if ans>max_ans:
        #                 max_ans = ans
        #             ans = 1
        # if ans>max_ans:
        #         max_ans = ans
        # return max_ans
        # Create a set of nums for O(1) lookups
        
        numSet = set(nums)
        longest = 0

        for num in numSet:
            # Only start counting if 'num' is the beginning of a sequence
            if num - 1 not in numSet:
                currentNum = num
                currentStreak = 1

                # Count the consecutive numbers following num
                while currentNum + 1 in numSet:
                    currentNum += 1
                    currentStreak += 1

                longest = max(longest, currentStreak)
                
        return longest