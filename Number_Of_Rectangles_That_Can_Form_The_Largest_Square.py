#You are given an array rectangles where rectangles[i] = [li, wi] represents the ith rectangle of length li and width wi.
#Return the number of rectangles that can make a square with a side length of maxLen.

class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        a = []
        for i in rectangles:
            a.append(min(i)) 
        return a.count(max(a))
