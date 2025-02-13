class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        visited = set()
        min_num = math.inf
        for num in nums:
            if num > 0:
                visited.add(num)
                if num < min_num:
                    min_num = num
        if min_num !=1:
            return 1
        # for i in range(len(visited)):    
        #     if (num-1 and num+1) not in visited:
        ans = 1
        while ans in visited:
            ans+=1
        return ans

        
