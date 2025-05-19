class Solution:
    def isHappy(self, n: int) -> bool: 
        store=set()
        while n!=1 and n not in store:
            store.add(n)
            n = sum(int(x)**2 for x in str(n))
        return n==1

if __name__ == "__main__":
    n = 19
    result = Solution().isHappy(n)
    # The expected output is True
    print("Result:", result)    