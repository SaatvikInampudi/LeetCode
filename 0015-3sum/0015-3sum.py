class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #TLE
        #Time complexity: O(n^3)
        #Space complexity: O(n^2)

        # index_dict = {}
        # for index,element in enumerate(nums):
        #     if element in index_dict:
        #         index_dict[element].append(index)
        #     else:
        #         index_dict[element] = [index]
        # # print(index_dict)
        
        # ans = []
        # left = 0
        # right = len(nums)-1

        # for _ in range(len(nums)-1):
        #     while left<right:
        #         # print(left,right)
        #         # print((0-(nums[left]+nums[right])))
        #         if (0-(nums[left]+nums[right])) in index_dict:
        #             for i in index_dict[(0-(nums[left]+nums[right]))]:
        #                 if i > left and i < right:
        #                     ans.append([nums[left],nums[i],nums[right]])
        #         right -= 1
        #     left += 1
        #     right = len(nums)-1

        # unique_set = {tuple(sorted(triplet)) for triplet in ans}
        # final_ans = [list(triplet) for triplet in unique_set]
        # return final_ans


        nums.sort()
        print(nums)
        ans = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i+1
            right = len(nums)-1
            while left<right:
                # print(left,right)
                if (nums[i]+nums[left]+nums[right]) == 0:
                    ans.append([nums[i],nums[left],nums[right]])
                    while left<right and nums[left]==nums[left+1]:
                        left+=1
                    while left<right and nums[right]==nums[right-1]:
                        right-=1
                    left += 1
                    right -= 1

                elif (nums[i]+nums[left]+nums[right]) < 0:
                    left += 1
                else:
                    right -= 1

        # unique_set = {tuple(triplet) for triplet in ans}
        # final_ans = [list(triplet) for triplet in unique_set]
        return ans
