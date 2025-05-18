class Solution(object):
    def removeDuplicates(self, nums):
        index=0
        val=nums[index]
        last=len(nums)
        i=1
        while i<last:
            if val==nums[i] or val>nums[i]:
                i+=1
            elif val<nums[i]:
                nums[index+1],nums[i]=nums[i],nums[index+1]
                index+=1
                val=nums[index]
        return index+1      

if __name__ == "__main__":
    nums = [1,1,2]
    result = Solution().removeDuplicates(nums)
    # The expected output is 2
    print("Result:", result)
    # The expected output is [1,2]
    print("Result:", nums[:result]) 