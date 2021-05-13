#Given a string array words, return the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. If no such two words exist, return 0.

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        a = [set(i) for i in words]
        l = [len(i) for i in words]
        m = 0
        for i in range(len(words)):
            for j in range(len(words)):
                if i!=j:
                    if not a[i] & a[j] and l[i]*l[j] > m:
                        m = l[i]*l[j]
        return m
