class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        minheap = []
        for i in nums:
            heapq.heappush(minheap, i)
        sorted_list = [heapq.heappop(minheap) for _ in range(len(minheap))]
        sorted_list = list(dict.fromkeys(sorted_list))
        print(sorted_list)

        ans = 1
        max_ans = 0
        for i in range(1,len(sorted_list)):
            if sorted_list[i] == sorted_list[i-1]+1:
                ans+=1
            else:
                if ans>max_ans:
                    max_ans = ans
                ans = 1
        if ans>max_ans:
                max_ans = ans
        return max_ans