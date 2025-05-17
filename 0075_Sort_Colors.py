class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l,r=0,len(nums)-1
        i=0
        while i<=r:
            if nums[i]==0:
                nums[i],nums[l]=nums[l],nums[i]
                l+=1
            elif nums[i]==2:
                nums[i],nums[r]=nums[r],nums[i]
                r-=1
                i-=1
            i+=1 
        return nums      

if __name__ == "__main__":
    nums = [2,0,2,1,1,0]
    result = Solution().sortColors(nums)
    # The expected output is [0,0,1,1,2,2]
    print("Result:", result)
