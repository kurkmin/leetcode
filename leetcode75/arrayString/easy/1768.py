class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""
        if len(word1) > len(word2):
            rep = len(word2)
            for i in range(rep):
                merged += word1[i]
                merged += word2[i]
            merged += word1[rep:]
        else: 
            rep = len(word1)
            for i in range(rep):
                merged += word1[i]
                merged += word2[i]
            merged += word2[rep:]
        return merged

        