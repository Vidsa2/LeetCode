class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        left=-1 # pointer for the first zero
        for i in range(len(nums)):
            if nums[i]==0 and left==-1: # first zero found
                left=i
            elif nums[i]!=0 and left !=-1:
                nums[left],nums[i]=nums[i],nums[left] # swap the zero with the non-zero
                left+=1
        return nums         
               
   
if __name__ == "__main__":
    nums = [0,1,0,3,12]
    result = Solution().moveZeroes(nums)
    # The expected output is [1,3,12,0,0]
    print("Result:", result)