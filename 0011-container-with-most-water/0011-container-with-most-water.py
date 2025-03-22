class Solution:
    def maxArea(self, height: List[int]) -> int:
        # left = 0
        # right = len(height)-1
        # vol = 0

        # while left<right:
        #     # print('hi')
        #     if ((right-left)*min(height[left],height[right])) > vol:
        #         vol = ((right-left)*min(height[left],height[right]))
        #         print(vol)

        #     if height[left] < height[right]:
        #         if height[left+1]>height[left]:
        #             left+=1
        #             # print('continue1')
        #             continue
        #         else:
        #             left +=2
        #             # print('continue2')
        #             continue
        #     elif height[left] > height[right]:
        #         if height[right-1]>height[right]:
        #             # print('check')
        #             right-=1
        #             continue
        #         else:
        #             right -=2
        #             # print('continue3')
        #             continue
        #     else:
        #         if height[left+1]>height[right-1]:
        #             left+=1
        #             # print('continue4')
        #             continue
        #         else:
        #             right-=1
        #             # print('continue5')
        #             continue

        #     # print('buff')
        #     left+=1
                
        # return vol

        left, right = 0, len(height) - 1
        vol = 0

        while left < right:
            # Calculate the current area
            vol = max(vol, (right - left) * min(height[left], height[right]))

            # Move the pointer at the smaller height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return vol