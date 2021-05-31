#Given an array of strings products and a string searchWord. We want to design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with the searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.
#Return list of lists of the suggested products after each character of searchWord is typed. 

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        ans = []
        c = []
        a = ''
        for i in searchWord:
            a += i
            for j in products:
                if j.startswith(a):
                    if len(c) < 3:
                        c.append(j)
            ans.append(c)
            c = []
        return ans
