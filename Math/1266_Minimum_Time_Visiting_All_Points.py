#On a 2D plane, there are n points with integer coordinates points[i] = [xi, yi]. Return the minimum time in seconds to visit all the points in the order given by points.

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans = 0
        s = points[0]
        
        for i in points[1:]:
            ans += max(abs(s[0] - i[0]), abs(s[1] - i[1]))
            s = i
        return ans
