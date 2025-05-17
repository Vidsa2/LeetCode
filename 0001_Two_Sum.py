# using two pointers and sorting 
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result=[] # to store the indices of the two numbers
        nums1=sorted(nums) # sort the array
        l,r=0,len(nums)-1 # left and right pointers
        while l<r:
            total=nums1[l]+nums1[r]
            if total ==target:
                break # found the two numbers
            elif total >target:
                r-=1 #  move the right pointer to the left
            else:
                l+=1 # move the left pointer to the right
        for i in range(len(nums)) :
            if nums[i]==nums1[l] or nums[i]==nums1[r]: # check if the number is one of the two numbers
                result.append(i)
        return result
if __name__ == "__main__":
    nums = [2,7,11,15]
    target = 9
    result = Solution().twoSum(nums, target)
    # The expected output is [0,1]
    print("Result:", result)