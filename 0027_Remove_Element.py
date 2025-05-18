class Solution(object):
    def removeElement(self, nums, val):
        i = 0
        last = len(nums) - 1

        while i <= last:
            if nums[i] == val:
                nums[i], nums[last] = nums[last], nums[i]
                last -= 1
            else:
                i += 1
        
        return last + 1  # because last is the index of the last valid element

if __name__ == "__main__":
    nums = [3,2,2,3]
    val = 3
    result = Solution().removeElement(nums, val)
    # The expected output is 2
    print("Result:", result)