#A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        res=[]
        for i in accounts:
            res.append(sum(i))
        return max(res)
         
'''     
        ans = 0
        a = 0
        for i in accounts:
            for j in i:
                a += j
                if a > ans:
                    ans = a
            a = 0        
        return ans     
'''
 
