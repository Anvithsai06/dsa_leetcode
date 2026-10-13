class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        res=""
        for i in words:
            sums=0
            for j in i:
                sums+=weights[ord(j)-97]
            res+=chr(25-(sums%26)+97)
        return res
