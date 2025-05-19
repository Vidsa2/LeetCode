class Solution(object):
    def romanToInt(self, s):
        roman ={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        val=0
        for i in range(len(s)):
            if i+1<len(s) and roman[s[i]]<roman[s[i+1]]:
                val-=roman[s[i]]
            else:
                val+=roman[s[i]]    
        return val
if __name__ == "__main__":
    s = "III"
    result = Solution().romanToInt(s)
    # The expected output is 3
    print("Result:", result)