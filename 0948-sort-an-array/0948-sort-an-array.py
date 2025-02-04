class Solution:

    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) >1:
            left = 0
            right = len(nums)
            mid = (left+right)//2
            nums1 = nums[left:mid]
            nums2 = nums[mid:right]

            # if len(nums) == 2:
            #     print(nums)

            #recurssion
            self.sortArray(nums1)
            self.sortArray(nums2)

            #merging
            # merge()

            i = 0
            j = 0
            k = 0
            while i < len(nums1) and j < len(nums2):
                if nums1[i] > nums2[j]:
                    nums[k] = nums2[j]
                    j+=1
                else:
                    nums[k] = nums1[i]
                    i+=1
                k+=1

            while i<len(nums1):
                nums[k] = nums1[i]
                i+=1
                k+=1

            while j<len(nums2):
                nums[k] = nums2[j]
                j+=1
                k+=1
        return nums

