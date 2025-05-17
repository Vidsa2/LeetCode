# LeetCode 392. Is Subsequence
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        j=0     # pointer for s
        for i in range(len(t)): # pointer for t
            if j<len(s) and t[i]==s[j] :
                j+=1
        if j==len(s):
            return True
        return False
    
if __name__ == "__main__":
    s = "abx"
    t = "ahbgdc"
    result = Solution().isSubsequence(s, t)
    print("Result:", result)