class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        count=0
        l,r=0,len(nums)-1
        while l<r:
            total=nums[l]+nums[r]
            if total==k:
                count+=1
                l+=1
                r-=1
            elif total>k:
                r-=1
            else:
                l+=1
        return count        
            
if __name__ == "__main__": 
    nums = [1,2,3,4]
    k = 5
    result = Solution().maxOperations(nums, k)
    # The expected output is 2
    print("Result:", result)      