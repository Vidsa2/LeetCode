class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap={} # to store the indices of the numbers

        for i,n in enumerate(nums):
            diff = target-n 
            if diff in hashmap: # check if the difference is in the hashmap
                return [hashmap[diff],i]
            hashmap[n]=i # store the index of the number
    


if __name__ == "__main__":
    nums = [2,7,11,15]
    target = 9
    result = Solution().twoSum(nums, target)
    # The expected output is [0,1]
    print("Result:", result)        