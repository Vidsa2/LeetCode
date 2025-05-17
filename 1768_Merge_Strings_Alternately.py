class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        x=max(len(word1),len(word2))
        word= []
        for i in range(x):
            if i<len(word1):
                word.append(word1[i]) 
            if i<len(word2):
                word.append(word2[i])
        return ''.join(word)


if __name__ == "__main__":
    word1 = "abc"
    word2 = "pqr"
    result = Solution().mergeAlternately(word1, word2)
    # The expected output is "apbqcr"
    print("Result:", result)    