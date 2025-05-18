class Solution(object):
    def merge(self, nums1, m, nums2, n):
        a = m + n - 1
        m -= 1
        n -= 1

        while n >= 0:
            if m >= 0 and nums1[m] > nums2[n]:
                nums1[a] = nums1[m]
                m -= 1
            else:
                nums1[a] = nums2[n]
                n -= 1
            a -= 1
        return nums1   


if __name__ == "__main__":
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    result = Solution().merge(nums1, m, nums2, n)
    # The expected output is [1,2,2,3,5,6]
    print("Result:", result)

