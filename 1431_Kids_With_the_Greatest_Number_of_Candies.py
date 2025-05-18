from typing import List
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxi = max(candies)
        result=[]
        for i in range (len(candies)):
            if candies[i]+extraCandies>=maxi:
                result.append(True)
            else:
                result.append(False)
        return result        
if __name__ == "__main__":
    candies = [2,3,5,1,3]
    extraCandies = 3
    result = Solution().kidsWithCandies(candies, extraCandies)
    # The expected output is [True, True, True, False, True]
    print("Result:", result)