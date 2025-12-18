class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if len(word1)==len(word2):
            max_l=min_l=len(word1)
        else:
            min_l = min(len(word1), len(word2))
            max_l = max(len(word1), len(word2))
        res = []
        for i in range(min_l):
            res.append(word1[i])
            res.append(word2[i])
        if len(word1)>len(word2):
            res.append(word1[min_l:])
        else:
            res.append(word2[min_l:])
        return "".join(res)

