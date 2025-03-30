class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # ans = []
        # for i in range(len(temperatures)):
        #     for j in range(i+1,len(temperatures)):
        #         if temperatures[j]>temperatures[i]:
        #             ans.append(j-i)
        #             break
        #     if len(ans) != i+1:
        #         ans.append(0)
        # return ans 

        # n = len(temperatures)
        # answer = [0] * n
        # stack = []
        
        # for curr_day, curr_temp in enumerate(temperatures):
        #     # Pop until the current day's temperature is not
        #     # warmer than the temperature at the top of the stack
        #     while stack and temperatures[stack[-1]] < curr_temp:
        #         prev_day = stack.pop()
        #         answer[prev_day] = curr_day - prev_day
        #     stack.append(curr_day)
        
        # return answer








        ans = [0] * len(temperatures)
        stack = []

        for curr_day,temp in enumerate(temperatures):
            # print(stack)
            while stack and stack[-1][1]<temp:
                prev = stack[-1][0]
                ans[prev] = curr_day - prev
                stack.pop()
            stack.append((curr_day,temp))

        return ans