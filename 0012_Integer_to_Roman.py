class Solution(object):
    def intToRoman(self, num):
        roman_list = [["I", 1],["IV", 4],["V", 5],["IX", 9],["X", 10],["XL", 40],["L", 50],
                    ["XC", 90],["C", 100],["CD", 400],["D", 500],["CM", 900],["M", 1000]]

        roman=""
        for symbol,val in  reversed(roman_list):
            if num//val:
                count=num//val
                roman+=(symbol*count)
                num=num%val
        return roman

if __name__ == "__main__":
    num = 1994
    result = Solution().intToRoman(num)
    # The expected output is "MCMXCIV"
    print("Result:", result)
