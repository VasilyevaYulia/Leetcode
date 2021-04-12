#You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi. Return the destination city, that is, the city without any path outgoing to another city.
#It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        ans = paths[0]
        for j in paths:
            for i in paths:
                if i[0] == ans[-1]:
                    ans.append(i[-1])   
                if i[-1] == ans[0]:
                    ans.insert(0, i[0])
        return ans[-1]
        '''
        s1 = set(x for x,y in paths)
        s2 = set(y for x,y in paths)
        return (s2 - s1).pop()
        '''
