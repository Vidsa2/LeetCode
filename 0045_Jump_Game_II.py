class Solution(object):
    def jump(self, nums):
        i=len(nums)-1
        count=0
        while i>0:
            j=0
            while j<i:
                if nums[j]>= i-j:
                    i=j
                    count+=1
                    break
                j+=1    

        return count



if __name__ == "__main__":
    nums = [2,3,1,1,4]
    result = Solution().jump(nums)
    # The expected output is 2
    print("Result:", result)